import json
import os
from time import sleep

# ALL THE EXT DATABASES
database = {}
with open(
    "extensions.json"
) as json_file:  # source: https://github.com/dyne/file-extension-list
    database = json.load(json_file)

# FILE LIST
files = os.listdir()


def _search_display(search_element: str):
    print(f"Searching for {search_element}", end="")
    for _ in range(10):
        print(".", end="")
        sleep(0.2)
    print("\nDone")


# ALL FUNCTIONS
def arrange_images():
    try:
        images = [
            file
            for file in files
            if os.path.splitext(file)[1].lower() in database["image"]
        ]
        _search_display("Images")
        if not images:
            print("No images found !!")
        else:
            print(f"Found {len(images)} images !!")
            _search_display("'Images' directory")
            if os.path.exists("Images") == False:
                print("Not Found !!\nSo creating", end="")
                for _ in range(10):
                    print(".", end="")
                sleep(0.2)
                os.mkdir("Images")
                print("Done!!")
            else:
                print("Found !!")
            for item in images:
                os.replace(item, f"Images/{item}")
            print(f"Successfully Moved {len(images)} image files in 'Images' folder")
    except Exception as error:
        print(f"\nI have encountered an unexpected error :(\nError : {error}")


def arrange_docs():
    try:
        documents = [
            file
            for file in files
            if os.path.splitext(file)[1].lower()
            in database["sheet"] + database["slide"] + database["text"]
        ]

        _search_display("Documents")
        print("Done")
        if not documents:
            print("No documents found !!")
        else:
            print(f"Found {len(documents)} documents !!")
            _search_display("'Documents' directory")
            if os.path.exists("Documents") is False:
                print("Not Found !!\nSo creating", end="")
                for _ in range(10):
                    print(".", end="")
                sleep(0.2)
                os.mkdir("Documents")
                print("Done!!")
            else:
                print("Found !!")
            for item in documents:
                os.replace(item, f"Documents/{item}")
            print(
                f"Successfully Moved {len(documents)} document files in 'Documents' folder"
            )

    except Exception as error:
        print(f"\nI have encountered an unexpected error :(\nError : {error}")


def arrange_videos():
    try:
        videos = [
            file
            for file in files
            if os.path.splitext(file)[1].lower() in database["video"]
        ]

        print("\nSearching for Videos", end="")
        for _ in range(10):
            print(".", end="")
            sleep(0.2)
        print("Done")
        if not videos:
            print("No videos found !!")
        else:
            print(f"Found {len(videos)} videos !!")
            _search_display("'Videos' directory")
            if os.path.exists("Videos") == False:
                print("Not Found !!\nSo creating", end="")
                for _ in range(10):
                    print(".", end="")
                sleep(0.2)
                os.mkdir("Videos")
                print("Done !!")
            for item in videos:
                os.replace(item, f"Videos/{item}")
            print(f"Successfully Moved {len(videos)} videos files in 'Videos' folder")
    except Exception as error:
        print(f"\nI have encountered an unexpected error :(\nError : {error}")


def arrange_audios():
    try:
        audios = [
            file
            for file in files
            if os.path.splitext(file)[1].lower() in database["audio"]
        ]
        print("\nSearching for Audios", end="")
        for _ in range(10):
            print(".", end="")
            sleep(0.2)
        print("Done")
        if not audios:
            print("No audio found !!")
        else:
            print(f"Found {len(audios)} audios !!")
            _search_display("'Audios' Directory")
            if os.path.exists("Audios") is False:
                print("Not Found !!\nSo creating", end="")
                for _ in range(10):
                    print(".", end="")
                sleep(0.2)
                os.mkdir("Audios")
                print("Done !!")
            else:
                print("Found !!")
            for item in audios:
                os.replace(item, f"Audios/{item}")
            print(f"Successfully Moved {len(audios)} audios files in 'Audios' folder")
    except Exception as error:
        print(f"\nI have encountered an unexpected error :(\nError : {error}")


def arrange_archive():
    try:
        archive = [
            file
            for file in files
            if os.path.splitext(file)[1].lower() in database["archive"]
        ]
        _search_display("Archives")
        if not archive:
            print("No archive found !!")
        else:
            print(f"Found {len(archive)} archive !!")
            _search_display("'Archives' directory")
            if os.path.exists("Archives") is False:
                print("Not Found !!\nSo creating", end="")
                for _ in range(10):
                    print(".", end="")
                sleep(0.2)
                os.mkdir("archive")
                print("Done!!")
            else:
                print("Found !!")
            for item in archive:
                os.replace(item, f"archive/{item}")
            print(f"Successfully Moved {len(archive)} archive files in 'Archives' folder")
    except Exception as error:
        print(f"\nI have encountered an unexpected error :(\nError : {error}")


def arrange_other():
    file_to_be_skipped = ["THE_ORGANIZER_3.2.exe", "DumpStack.log.tmp"]
    others_ext = []
    try:
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if (
                ext
                not in database["image"]
                + database["sheet"]
                + database["slide"]
                + database["text"]
                + database["video"]
                + database["audio"]
                + database["archive"]
                and os.path.isfile(file)
                and os.path.basename(file) not in file_to_be_skipped
            ):
                others_ext.append(file)
        _search_display("Other files")
        if not others_ext:
            print("No others files found !!")
        else:
            print(f"Found {len(others_ext)} others files !!")
            _search_display("'Others' directory")
            if os.path.exists("Others") == False:
                print("Not Found !!\nSo creating", end="")
                for _ in range(10):
                    print(".", end="")
                sleep(0.2)
                os.mkdir("Others")
                print("Done !!")
            else:
                print("Found !!")
            for item in others_ext:
                os.replace(item, f"Others/{item}")
            print(
                f"Successfully Moved {len(others_ext)} others files in 'Others' folder"
            )
    except Exception as error:
        print(f"\nI have encountered an unexpected error :(\nError : {error}")


def delete_empty_folder():
    try:
        empty_folders = []
        count = 0
        _search_display("Empty folders")
        for file in files:
            if os.path.isdir(file) and len(os.listdir(file)) == 0:
                empty_folders.append(file)
                count += 1
                os.rmdir(file)
        print("Done !!")
        if not empty_folders:
            print(f"Successfully deleted {count} empty folders\n")
        else:
            print("No empty folders found !!\n")
    except Exception as error:
        print(f"\nI have encountered an unexpected error :(\nError : {error}")


be_organised_text = (
    "\n\n\t\t\t\t THANKS FOR CHOOSING ORGANIZER ^_^\n\t\t\t\t\t #be_organized ✌️"
)
if __name__ == "__main__":
    print(
        "\n\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx WELCOME TO ORGANIZER xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    )
    print("\t\t\t\t\t\t\t\t\t\t   Made by Biswajit Mishra")
    print(
        "\n\nWhat is does --> This is a organizer program which will orgranize all the mess in your system\n"
    )
    print("Note : Press 'q' to exit anytime\n")
    print(f"ATTENTION !!\nCurrent working directory is : {os.getcwd()}\n")
    while True:
        print(
            "Options Available:-",
            "1. Arrange Images",
            "2. Arrange Documents",
            "3. Arrange Videos",
            "4. Arrange Audio Files",
            "5. Arrange Archives",
            "6. Other Files",
            "7. Clear Empty folders",
            "8. Arrange All File Type",
            "",
            "So BOSS !! What you wanna do?",
            "Ans:",
            sep="\n",
            end=" ",
        )
        user_choice = input()
        if user_choice.lower() == "q":
            print(be_organised_text)
            break
        elif user_choice == "1":
            arrange_images()
            print(be_organised_text)
        elif user_choice == "2":
            arrange_docs()
            print(be_organised_text)
        elif user_choice == "3":
            arrange_videos()
            print(be_organised_text)
        elif user_choice == "4":
            arrange_audios()
            print(be_organised_text)
        elif user_choice == "5":
            arrange_archive()
            print(be_organised_text)
        elif user_choice == "6":
            arrange_other()
        elif user_choice == "7":
            delete_empty_folder()
        elif user_choice == "8":
            arrange_images()
            arrange_docs()
            arrange_videos()
            arrange_audios()
            arrange_other()
            delete_empty_folder()
            print(be_organised_text)
        else:
            print("\nPlease enter a valid input !!\n")
