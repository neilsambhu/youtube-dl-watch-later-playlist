from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from termcolor import colored
import getpass
import subprocess
import os

download_folder = '~/Downloads/'
download_folder = 'G:/My Drive/File Transfers/Transfer To Individuals/To Neil/2022 04 16 YouTube Watch Later/'


# def get_google_username():
#     # return input('ᕙ(⇀‸↼‶)ᕗ Enter your google username: ')


# def get_google_password():
#     # return getpass.getpass('ᕙ(⇀‸↼‶)ᕗ Enter your google password: ')


# def start_browser():
#     chrome_options = Options()
#     chrome_options.add_argument("--disable-extensions")
#     chrome_options.add_argument("--ignore-certificate-errors")
#     chrome_options.add_argument("--disable-plugins-discovery")
#     chrome_options.add_argument("--incognito")
#     return webdriver.Chrome(options=chrome_options)


# def login_to_google(driver, username, password):
#     driver.get("https://stackoverflow.com/users/signup")
#     driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()

#     verify_username(username)
#     verify_password(password)

#     # Waits until redirect to stackoverflow.com occurs
#     wait = WebDriverWait(driver, 300)
#     wait.until(EC.url_contains("stackoverflow.com"))
#     print(colored('Login successful.', 'green'))


# def verify_username(username):
#     login_field = WebDriverWait(driver, 60).until(
#         EC.element_to_be_clickable((By.ID, 'identifierId'))
#     )
#     while True:
#         # Enters username and clicks next button
#         login_field.send_keys(username)
#         driver.find_element_by_id('identifierNext').click()

#         try:
#             # Checks for invalid username warning
#             warning = WebDriverWait(driver, 3).until(
#                 EC.visibility_of_element_located(
#                     (By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[2]/div[2]'))
#             )
#             if warning:
#                 print(colored('Warning! Google Account not found.', 'red'))
#                 username = get_google_username()
#                 login_field.clear()
#                 continue
#         except(TimeoutException):
#             print(colored('Username verified.', 'green'))
#             break


# def verify_password(password):
#     password_field = WebDriverWait(driver, 60).until(
#         EC.element_to_be_clickable((By.XPATH, '//input[@type="password"]'))
#     )
#     while True:
#         # Enters password and clicks next button
#         password_field.send_keys(password)
#         driver.find_element_by_id('passwordNext').click()

#         try:
#             # Checks for invalid password warning
#             warning = WebDriverWait(driver, 3).until(
#                 EC.visibility_of_element_located(
#                     (By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[2]'))
#             )
#             if warning:
#                 print(colored('Warning! Wrong password.', 'red'))
#                 password = get_google_password()
#                 continue
#         except(TimeoutException):
#             print(colored('Password verified.', 'green'))
#             break


def scrape_watch_later_playlist(driver):
    driver.get("https://www.youtube.com/playlist?list=WL")
    videos = WebDriverWait(driver, 60).until(
        EC.presence_of_all_elements_located((By.XPATH, '//*[@id="content"]/a'))
    )
    urls = []

    for video in videos:
        url = video.get_attribute('href')
        url = url.split('&list=WL&index=')
        url = url[0]
        urls.append(url)
    return urls
def scrape_watch_later_playlist2():
    urls = []
    import pyautogui


def run_terminal_cmd(cmd):
    process = subprocess.run(cmd, shell=True)
    if process.returncode != 0:
        print(colored('Error running cmd!', 'red'))
        return
    else:
        return process.stdout


if __name__ == '__main__':
    print('ᕙ(⇀‸↼‶)ᕗ starting download script for youtube watch later playlist.')
    # username = get_google_username()
    # password = get_google_password()

    # driver = start_browser()
    # from webdriver_manager.chrome import ChromeDriverManager
    # driver = webdriver.Chrome(ChromeDriverManager().install())

    # login_to_google(driver, username, password)
    # videos = scrape_watch_later_playlist(driver)
    # videos = scrape_watch_later_playlist2()
    '''
    // Execute this in the console of on your own playlist

    var videos = document.querySelectorAll('.yt-simple-endpoint.style-scope.ytd-playlist-video-renderer');
    var r = [];
    var json = [];

    r.forEach.call(videos, function(video) {
        var url = 'https://www.youtube.com' + video.getAttribute('href');
        url = url.split('&list=WL&index=');
        url = url[0];
        json.push(url);
    });
    console.log(json)
    '''    
    videos = [
        # "https://www.youtube.com/watch?v=-f-CFQxaUY4",
        # "https://www.youtube.com/watch?v=g0qirWh1Y0A",
        # "https://www.youtube.com/watch?v=r5HXPxB837s",
        # "https://www.youtube.com/watch?v=UQ7ukdOoanI",
        # "https://www.youtube.com/watch?v=VarGDqd0274",
        # "https://www.youtube.com/watch?v=wsLnPRUUGhQ",
        # "https://www.youtube.com/watch?v=R2u8pw93fwk",
        # "https://www.youtube.com/watch?v=mtDUonqHVyo",
        # "https://www.youtube.com/watch?v=csF-HlAJgis",
        # "https://www.youtube.com/watch?v=imO33X-SbDY",
        # "https://www.youtube.com/watch?v=j3y1UGV2Mls",
        # "https://www.youtube.com/watch?v=0foq0Krn9yI",
        # "https://www.youtube.com/watch?v=N1PPKa3S74g",
        # "https://www.youtube.com/watch?v=1Hgs3hEZnDQ",
        # "https://www.youtube.com/watch?v=--kxrdJTjjI",
        "https://www.youtube.com/watch?v=atJz8HaA5Cc",
        "https://www.youtube.com/watch?v=5Q8GyZN8vgI",
        "https://www.youtube.com/watch?v=SCV7R7dfAv8",
        "https://www.youtube.com/watch?v=hrNtLDVVcoU",
        "https://www.youtube.com/watch?v=d8SEL6Xl2ww",
        "https://www.youtube.com/watch?v=VxDEpLLxgOs",
        "https://www.youtube.com/watch?v=yQjMjnMk-14",
        "https://www.youtube.com/watch?v=pJ3gZyw2kb0",
        "https://www.youtube.com/watch?v=4XsIha-V6JY",
        "https://www.youtube.com/watch?v=WR9yqC8HQGg",
        "https://www.youtube.com/watch?v=FEK-vW8IQzA",
        "https://www.youtube.com/watch?v=kIApsl6wFFQ",
        "https://www.youtube.com/watch?v=NwhewTM3kes",
        "https://www.youtube.com/watch?v=fVw3yF3Rsfs",
        "https://www.youtube.com/watch?v=nmARwpokZ-k",
        "https://www.youtube.com/watch?v=mtn7mzH5WDY",
        "https://www.youtube.com/watch?v=8et3RnIrzyM",
        "https://www.youtube.com/watch?v=udxx5aZn5Vs",
        "https://www.youtube.com/watch?v=-slnr4TGA4Y",
        "https://www.youtube.com/watch?v=L6IonRH1-ow",
        "https://www.youtube.com/watch?v=7t_X_rkCHuM",
        "https://www.youtube.com/watch?v=M5QJHZvDHEw",
        "https://www.youtube.com/watch?v=OSAGXxAzMt4",
        "https://www.youtube.com/watch?v=dtQGajYtLm4",
        "https://www.youtube.com/watch?v=VVKrlW_nyBI",
        "https://www.youtube.com/watch?v=AqCwSwyq8u0",
        "https://www.youtube.com/watch?v=Qq7P-zeJmO8",
        "https://www.youtube.com/watch?v=Vu3zcyBQbm0",
        "https://www.youtube.com/watch?v=HJlQ_jpPOJ0",
        "https://www.youtube.com/watch?v=weNoxPQVj1E",
        "https://www.youtube.com/watch?v=tX6XSs2T5Go",
        "https://www.youtube.com/watch?v=xlCDxXXSS5A",
        "https://www.youtube.com/watch?v=AolW2szNfNc",
        "https://www.youtube.com/watch?v=bit5cYSoqEo",
        "https://www.youtube.com/watch?v=jT0vdck7i5Q",
        "https://www.youtube.com/watch?v=stZzEfFCuBs",
        "https://www.youtube.com/watch?v=iJbrkN9_73M",
        "https://www.youtube.com/watch?v=fFF2GvkQfNU",
        "https://www.youtube.com/watch?v=unguMlKkc74",
        "https://www.youtube.com/watch?v=qpCB9g_O-uM",
        "https://www.youtube.com/watch?v=aLmEyfz3ntc",
        "https://www.youtube.com/watch?v=9RnE86rx6O4",
        "https://www.youtube.com/watch?v=0FgisLkb8LM",
        "https://www.youtube.com/watch?v=6PwEAQPcuVo",
        "https://www.youtube.com/watch?v=9u3lT8DzFaA",
        "https://www.youtube.com/watch?v=k6pUhiIer2E",
        "https://www.youtube.com/watch?v=LJiubxirYNE",
        "https://www.youtube.com/watch?v=JjLVn8W0lBc",
        "https://www.youtube.com/watch?v=nAC5wImVF-4",
        "https://www.youtube.com/watch?v=umflaqVTJUc",
        "https://www.youtube.com/watch?v=an8dcTk1fSA",
        "https://www.youtube.com/watch?v=P7A8afB57qA",
        "https://www.youtube.com/watch?v=aUPNOaSdB10",
        "https://www.youtube.com/watch?v=_9I49wgZ5U0",
        "https://www.youtube.com/watch?v=cVsaDOLfQPs",
        "https://www.youtube.com/watch?v=rlKQUfs3Pnk",
        "https://www.youtube.com/watch?v=CqlqOSCZmkI",
        "https://www.youtube.com/watch?v=A_COFYJNdxk",
        "https://www.youtube.com/watch?v=KAtvVb8piyc",
        "https://www.youtube.com/watch?v=OM-AeVyW1kk",
        "https://www.youtube.com/watch?v=AluKoVYAPgs",
        "https://www.youtube.com/watch?v=YeDgfHtTHPA",
        "https://www.youtube.com/watch?v=aa59LcP7kkY",
        "https://www.youtube.com/watch?v=fobJCljIENo",
        "https://www.youtube.com/watch?v=1fRehcmRM-g",
        "https://www.youtube.com/watch?v=-2jy_CQ0wIU",
        "https://www.youtube.com/watch?v=6QU65cuCuXo",
        "https://www.youtube.com/watch?v=YChRmYT98Wk",
        "https://www.youtube.com/watch?v=sEmcqxBuopY",
        "https://www.youtube.com/watch?v=JbY8BtcchjU",
        "https://www.youtube.com/watch?v=4ssiEkfG0uQ",
        "https://www.youtube.com/watch?v=3QrOK8DC3RE",
        "https://www.youtube.com/watch?v=1NgleTuXSi0",
        "https://www.youtube.com/watch?v=TrTZgv3s4A0",
        "https://www.youtube.com/watch?v=hppd9apHqfM",
        "https://www.youtube.com/watch?v=7dVVbyTurt8",
        "https://www.youtube.com/watch?v=zt-64z2QKto",
        "https://www.youtube.com/watch?v=eeNSg5QVlYE",
        "https://www.youtube.com/watch?v=ivFIGvjx1lY",
        "https://www.youtube.com/watch?v=doRg9Z_Huvc",
        "https://www.youtube.com/watch?v=I4PyZkOnvnk",
        "https://www.youtube.com/watch?v=1BsWFzgUBQY",
        "https://www.youtube.com/watch?v=_cgtAw21MM4",
        "https://www.youtube.com/watch?v=IUY9hln2zVc",
        "https://www.youtube.com/watch?v=BIwhVshA1Nk"
    ]
    for idx,video in enumerate(videos):
        print(f"{idx} of {len(videos)}")
        prefix = "youtube-dl -i -c "
        # output = "-o \"" + download_folder + "%(title)s.%(ext)s\" "
        # output = "-o '" + download_folder + "{} %(title)s.%(ext)s' ".format(idx)
        # output = "-o \"" + download_folder + "%(playlist_index)s%(title)s.%(ext)s\" "
        # output = "-o \"" + download_folder + "%(epoch)s%(title)s.%(ext)s\" "
        # output = "-o \"" + download_folder + "%(autonumber)s%(title)s.%(ext)s\" "
        # output = "-o \"" + download_folder + f"{idx:{0}{3}} %(title)s.%(ext)s\" "
        # output = "-o \"" + download_folder + f"{idx:{0}{3}} %(uploader)s - %(creator)s - %(title)s.%(ext)s\" "
        # output = "-o \"" + download_folder + f"{idx:{0}{3}}_%(channel)s_%(title)s.%(ext)s\" "
        output = "-o \"" + download_folder + f"{idx:{0}{3}}_%(channel)s_\'%(title)s\'.%(ext)s\" "
        # quality = "-f \"bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]\" "
        # quality = "-f \"bestvideo[height<=1080]\" "
        # quality = "-f \"best\" "
        # quality = "-f 22 "
        # quality = "-f \"bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio\" --merge-output-format mp4 "
        # quality = "-f \"bestvideo[ext=mp4]+bestaudio[ext=mp4]/bestvideo+bestaudio\" --merge-output-format mp4 "
        # quality = "-f \"bestvideo[ext=mp4]+bestaudio[ext=mp4]/bestvideo+bestaudio\" --merge-output-format mp4 --write-sub "
        # quality = "-f \"bestvideo[ext=mp4]+bestaudio[ext=mp4]/bestvideo+bestaudio\" --merge-output-format mp4 --write-auto-sub --embed-subs "
        quality = "-f \"bestvideo[ext=mp4]+bestaudio[ext=mp4]/bestvideo+bestaudio\" --merge-output-format mp4 --write-auto-sub --sub-format \"srt\" "
        quality = "-f \"bestvideo[ext=mp4]+bestaudio[ext=mp4]/bestvideo+bestaudio\" --merge-output-format mp4 --write-auto-sub --convert-subs \"srt\" "
        # quality = ""
        cmd = prefix + output + quality + video
        print(cmd)
        run_terminal_cmd(cmd)
        break
