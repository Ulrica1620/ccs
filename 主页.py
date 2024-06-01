import streamlit as st
# from rembg import remove
from PIL import Image
from io import BytesIO
import base64
import pytz
from datetime import datetime

import socket
import google_auth_httplib2
import httplib2
import pandas as pd
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import HttpRequest


st.set_page_config(layout="wide", page_title="Hello Page")
# Add custom CSS to hide the GitHub icon
hide_github_icon = """
GithubIcon {
  visibility: hidden;
}
"""
st.markdown(hide_github_icon,unsafe_allow_html=True)

st.title("🎸 陈楚生&花生资源库")
st.markdown(
    """
    这是一个陈楚生相关信息总结网站，将包含多个板块。
    ***音乐作品安利，奖项科普，音综战绩，破除洗脑包，...*** ，欢迎朋友们一起建设。

    👈 **请点开左侧小箭头查看更多内容。**

    👈 **要联系我，请在下方留言。**

    👈 **目前进度：音综战绩。**
    """
)
st.markdown("\n")
st.markdown('\n')
st.markdown('\n')

def sidebar_bg(side_bg):
 
   side_bg_ext = 'png'
 
   st.markdown(
      f"""
      <style>
      [data-testid="stSidebar"] > div:first-child {{
          background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()});
      }}
      </style>
      """,
      unsafe_allow_html=True,
      )
 
#调用
# sidebar_bg('/Users/wcheng/Desktop/ticket/陈楚生/ccs/image/sidebar_bg.png')



st.title("🦈 陈楚生简介")
st.markdown(
    """
    写写写写写写到头大
    """
)
st.markdown("\n")
st.markdown('\n')
st.markdown('\n')



def main_bg(main_bg):
    main_bg_ext = "jpg"
    st.markdown(
        f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )
 
#调用
main_bg('./image/background.png')


st.subheader('🙌 留下评论与建议')

st.markdown("\n")
st.markdown('\n')
st.markdown('\n')

socket.setdefaulttimeout(15 * 60)

SCOPE = "https://www.googleapis.com/auth/spreadsheets"
SPREADSHEET_ID = "129tth_W1xShuSur-efAVtMpzp1bW24KcL9ZGUauwG7A"# "1RtSCrn232rwYZ_DZAOU1lqzEha-2zP0ZjMf7342YZBA" #"1rkMVLvh3JrBq_tbi4Ho0qjCDAP3vYdNuWOEjYpkJLNU"
SHEET_NAME = "Database"
GSHEET_URL = f"https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}"




@st.cache_resource()
def connect():
    # Create a connection object.
    credentials = service_account.Credentials.from_service_account_info(
        st.secrets["gcp_service_account"],
        scopes=[SCOPE],
    )

    # Create a new Http() object for every request
    def build_request(http, *args, **kwargs):
        new_http = google_auth_httplib2.AuthorizedHttp(
            credentials, http=httplib2.Http()
        )
        return HttpRequest(new_http, *args, **kwargs)

    authorized_http = google_auth_httplib2.AuthorizedHttp(
        credentials, http=httplib2.Http()
    )
    service = build(
        "sheets",
        "v4",
        requestBuilder=build_request,
        http=authorized_http,
    )
    gsheet_connector = service.spreadsheets()
    return gsheet_connector


def collect(gsheet_connector) -> pd.DataFrame:
    values = (
        gsheet_connector.values()
        .get(
            spreadsheetId=SPREADSHEET_ID,
            range=f"{SHEET_NAME}!A:C",
        )
        .execute()
    )

    df = pd.DataFrame(values["values"])
    df.columns = df.iloc[0]
    df = df[1:]
    return df


def insert(gsheet_connector, row) -> None:
    values = (
        gsheet_connector.values()
        .append(
            spreadsheetId=SPREADSHEET_ID,
            range=f"{SHEET_NAME}!A:C",
            body=dict(values=row),
            valueInputOption="USER_ENTERED",
        )
        .execute()
    )

COMMENT_TEMPLATE_MD = """{} - {}
> {}"""




def timezone_change(time_str, src_timezone, dst_timezone=None):
    """
    将任一时区的时间转换成指定时区的时间
    如果没有指定目的时区，则默认转换成当地时区

    :param time_str:
    :param src_timezone: 要转换的源时区，如"Asia/Shanghai"， "UTC"
    :param dst_timezone: 要转换的目的时区，如"Asia/Shanghai", 如果没有指定目的时区，则默认转换成当地时区
    :param dst_timezone: 时间格式
    :return: str, 字符串时间格式
    """
    time_format = "%Y-%m-%d %H:%M:%S"

    # 将字符串时间格式转换成datetime形式
    old_dt = datetime.strptime(time_str, time_format)

    # 将源时区的datetime形式转换成GMT时区(UTC+0)的datetime形式
    dt = pytz.timezone(src_timezone).localize(old_dt)
    utc_dt = pytz.utc.normalize(dt.astimezone(pytz.utc))

    # 将GMT时区的datetime形式转换成指定的目的时区的datetime形式
    if dst_timezone:
        _timezone = pytz.timezone(dst_timezone)
        new_dt = _timezone.normalize(utc_dt.astimezone(_timezone))
    else:
        # 未指定目的时间，默认转换成当地时区
        new_dt = utc_dt.astimezone()
    # 转换成字符串时间格式
    return new_dt.strftime(time_format)
# Comments part

conn = connect()
comments = collect(conn)

with st.expander("💬 评论区"):

    # Show comments

    st.write("**历史评论:**")

    for index, entry in enumerate(comments.itertuples()):
        st.markdown(COMMENT_TEMPLATE_MD.format(entry.name, entry.date, entry.comment))

        is_last = index == len(comments) - 1
        is_new = "just_posted" in st.session_state and is_last
        if is_new:
            st.success("☝️ 你的评论已成功发布。")

    st.markdown("\n")
    st.markdown('\n')
    st.markdown('\n')

    # Insert comment

    st.write("**发布你的看法:**")
    form = st.form("comment")
    name = form.text_input("用户名")
    comment = form.text_area("评论")
    submit = form.form_submit_button("发布")

    if submit:
        date = str(datetime.now(tz=pytz.timezone('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S"))
        # st.markdown(date)
        # date = timezone_change(date, src_timezone="America/Los_Angeles", dst_timezone="Asia/Shanghai")
        insert(conn, [[name, comment, date]])
        if "just_posted" not in st.session_state:
            st.session_state["just_posted"] = True
        st.experimental_rerun()








c1, c2 = st.columns(2)

with c1:
    st.info('**陈楚生&花生**', icon="🥜")

with c2:
    st.info('**Contact: [@仓仓仓鼠w ](https://weibo.com/u/3216459360)**', icon="📩")



