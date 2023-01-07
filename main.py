# imports
from downloader import *

def main():
    console = Console()
    console.print("[red]Youtube[/]Downloader", justify="center")
    # getting video
    video = (
        input("Link of the video (blank = get from clipboard): ")
        or pyperclip.paste()
    )
    print(f"Url: {video}")
    # getting quality
    options = ["MP3 Audio", "Lowest Quality", "Max Quality"]
    print("OPTIONS:")
    ShowOptions(options)
    available_options = dir(Downloader)[-3:]
    option = available_options[IntPrompt.ask("Choose the option",choices=[str(i) for i in range(3)],default=0)]

    # getting path
    try:
        with open("paths.json") as f:
            data = json.load(f)
        paths = CheckPaths(data["paths"])
        if paths:
            print("PATHS: ")
            ShowOptions(paths)
    except BaseException:
        print("Error while reading paths.json")
    path = input("Choose a custom or existing paths(blank = ./):") or "./"
    if path.isnumeric() and int(path) <= len(paths):
        d = Downloader(video, paths[int(path)])
    else:
        d = Downloader(video, path)
    print(f"Downloading {d.title}...")
    getattr(d, option)()
    print("Video Downloaded!")


if __name__ == "__main__":
    main()