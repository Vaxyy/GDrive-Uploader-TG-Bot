import os

class Config:
  ENV = bool(os.environ.get('ENV', False))
  if ENV:
    BOT_TOKEN = os.environ.get('BOT_TOKEN')
    APP_ID = os.environ.get('APP_ID')
    API_HASH = os.environ.get('API_HASH')
    DATABASE_URL = os.environ.get('DATABASE_URL')
  else:
    BOT_TOKEN = '5076719969:AAF-dO7u1Qqvhd5s3whqG39GgTLFx1Zy4A8' # Get it from https://t.me/BotFather
    APP_ID = '7712824' # Get it from my.telegram.org/apps
    API_HASH = '2d3673e18b462f8032c4eea2f50b9f52' # Get it from my.telegram.org/apps
    DATABASE_URL = 'postgres://qmqeurallwuewg:f510689eb9a8e7d9a4f53aa5a65cfdad8f2bb7914973d1da7efcbcf64aecfad1@ec2-18-233-114-179.compute-1.amazonaws.com:5432/d7gda9b4a9n866' # SQL Database URL / Heroku Postgres URL


class Messages:

    START_MSG = "**Hi there {}.**\n__I'm Google Drive Uploader Bot.You can use me to upload any file / video to Google Drive from direct link or Telegram Files.__\n__You can know more from /help.__"

    HELP_MSG = [
        ".",
        "**Google Drive Uploader**\n__I can upload files from direct link or Telegram Files to your Google Drive. All i need is to authenticate me to your Google Drive Account and send a direct download link or Telegram File.__\n\nI have more features... ! Wanna know about it ? Just walkthrough this tutorial and read the messages carefully.",
        
        "**Authenticating Google Drive**\n__Send the /auth commmand and you will receive a URL, visit URL and follow the steps and send the received code here. Use /revoke to revoke your currently logged Google Drive Account.__",
        
        "**Direct Links**\n__Send me a direct download link for a file and i will download it on my server and Upload it to your Google Drive Account. You can rename files before uploading to GDrive Account. Just send me the URL and new filename separated by ' | '.__\n\n**__Examples:__**\n```https://example.com/AFileWithDirectDownloadLink.mkv | New FileName.mkv```",
        
        "**Telegram Files**\n__To Upload telegram files in your Google drive Account just send me the file and i will download and upload it to your Google Drive Account. Note: Telegram Files Downloading are slow. it may take longer for big files.__",
        
        "**Custom Folder for Upload**\n__Want to upload in custom folder or in__ **TeamDrive** __ ?\nUse /setfolder {Folder ID / TeamDrive ID / Folder UrL} to set custom upload folder.\nAll the files are uploaded in the custom folder you provide.__",
        
        "**Copy Google Drive Files**\n__Yes, Clone or Copy Google Drive Files.\nUse /copy {File id / Folder id or URL} to copy Google Drive Files in your Google Drive Account.__",
        
        "**Rules & Precautions**\n__1. Don't copy BIG Google Drive Files/Folders. It may hang the bot and your files maybe damaged.\n2. Send One request at a time unless bot will stop all processes.\n3. Don't send slow links @transload it first.\n4. Don't misuse, overload or abuse this free service.__",
        
        "**Developed by @viperadnan**"
        ]
