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

# auto save
subprocess.run("git commit -a -m \"auto save\"",capture_output=False)
subprocess.run("git push",capture_output=False)

download_folder = '~/Downloads/'
download_folder = 'G:/My Drive/File Transfers/Transfer To Individuals/To Neil/YouTube Downloads/2022 04 16 Watch Later/'
download_folder = 'G:/My Drive/File Transfers/Transfer To Individuals/To Neil/YouTube Downloads/2022 04 19 Dr. Boz/'
# download_folder = 'G:/My Drive/File Transfers/Transfer To Individuals/To Neil/YouTube Downloads/2022 04 19 Watch Later/'


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

    # print(f"{idx} of {len(videos)}")
    # prefix = "youtube-dl -i -c "
    # username = ""
    # password = ""
    # prefix = f"yt-dlp -i -u {username} -p {password} --cookies youtube.com_cookies.txt --compat-options no-live-chat --download-archive myarchive.txt "
    # prefix = f"yt-dlp -i --cookies youtube.com_cookies.txt --compat-options no-live-chat --download-archive myarchive.txt --config-locations yt-dlp.conf "
    # prefix = f"yt-dlp -i --config-locations yt-dlp.conf --cookies youtube.com_cookies.txt --sub-langs en.* --download-archive myarchive.txt "
    # add "--sleep-subtitles SECONDS" to hopefully prevent "Unable to download video subtitles for 'en': HTTP Error 429: Too Many Requests"
    prefix = f"yt-dlp -i --config-locations yt-dlp.conf --cookies youtube.com_cookies.txt --sub-langs en.* --download-archive myarchive.txt --sleep-subtitles 10 "
    # output = "-o \"" + download_folder + "%(title)s.%(ext)s\" "
    # output = "-o '" + download_folder + "{} %(title)s.%(ext)s' ".format(idx)
    # output = "-o \"" + download_folder + "%(playlist_index)s%(title)s.%(ext)s\" "
    # output = "-o \"" + download_folder + "%(epoch)s%(title)s.%(ext)s\" "
    # output = "-o \"" + download_folder + "%(autonumber)s%(title)s.%(ext)s\" "
    # output = "-o \"" + download_folder + f"{idx:{0}{3}} %(title)s.%(ext)s\" "
    # output = "-o \"" + download_folder + f"{idx:{0}{3}} %(uploader)s - %(creator)s - %(title)s.%(ext)s\" "
    # output = "-o \"" + download_folder + f"{idx:{0}{3}}_%(channel)s_%(title)s.%(ext)s\" "
    # output = "-o \"" + download_folder + f"%(playlist_index)s_%(channel)s_\'%(title)s\'.%(ext)s\" "
    # output = "-o \"" + os.path.join(download_folder, f"%(playlist_index)s_%(channel)s_\'%(title)s\'.%(ext)s\" ")
    output = "-o \"" + os.path.join(download_folder, f"%(autonumber)s_%(channel)s_\'%(title)s\'.%(ext)s\" ")
    # quality = "-f \"bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]\" "
    # quality = "-f \"bestvideo[height<=2160][ext=mp4]+bestaudio[ext=mp4]\" "
    # quality = "-f \"bestvideo[height<=1080]\" "
    # quality = "-f \"best\" "
    # quality = "-f 22 "
    # quality = "-f \"bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio\" --merge-output-format mp4 "
    # quality = "-f \"bestvideo[ext=mp4]+bestaudio[ext=mp4]/bestvideo+bestaudio\" --merge-output-format mp4 "
    # quality = "-f \"bestvideo[ext=mp4]+bestaudio[ext=mp4]/bestvideo+bestaudio\" --merge-output-format mp4 --write-sub "
    # quality = "-f \"bestvideo[ext=mp4]+bestaudio[ext=mp4]/bestvideo+bestaudio\" --merge-output-format mp4 --write-auto-sub "
    quality = "-f \"bestvideo[ext=mp4]+bestaudio[ext=mp4]/bestvideo+bestaudio\" --merge-output-format mp4 --write-auto-sub --embed-subs "
    # quality = "-f \"bestvideo[ext=mp4]+bestaudio[ext=mp4]/bestvideo+bestaudio\" --merge-output-format mp4 --write-auto-sub --sub-format \"srt\" "
    # quality = "-f \"bestvideo[ext=mp4]+bestaudio[ext=mp4]/bestvideo+bestaudio\" --merge-output-format mp4 --write-auto-sub --convert-subs \"srt\" "
    # quality = ""
    video = ":ytwatchlater "
    # need to add "--playlist-reverse" option to download videos from oldest to newest
    quality += "--playlist-reverse "
    video = "https://www.youtube.com/c/DrBozAnnetteBosworthMD/videos?view=0&sort=da&flow=grid "
    cmd = prefix + output + quality + video

    print(cmd)
    run_terminal_cmd(cmd)