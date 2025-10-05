import yt_dlp

# URL of the YouTube video
url = ["https://youtu.be/fhoDRB53DwY?si=f23yyuFSWAODUbi_","https://youtu.be/5xFRg_TzlAg?si=x_IDlE5cdj6p89xf","https://youtu.be/cvsbHZcDx8w?si=1zri8iuHreTxnKtZ","https://youtu.be/1dkfuga2_Ps?si=Ps77MDsUZ_Fqfgt0","https://youtu.be/-XwZpYIyCEA?si=b0HV2wgU8av0XfPE"]

# Options for download
ydl_opts = {
    'format': 'best',                 # best quality
    'outtmpl': 'videos/%(title)s.webm'  # save in Downloads folder
}

for i in url:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([i])

    print("Download Completed! Check your Downloads folder.")
