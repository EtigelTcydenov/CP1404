import wikipedia

def main():
    wikipedia.set_lang("en")

    while True:
        search_input = input("Enter a page title or search phrase: ")

        if not search_input:
            break

        try:
            page = wikipedia.page(search_input, auto_suggest=False)
            print("Title:", page.title)
            print("Summary:")
            print(page.summary)
            print("URL:", page.url)
        except wikipedia.exceptions.DisambiguationError as e:
            print("Disambiguation page encountered. Options:")
            for option in e.options:
                print("-", option)
        except wikipedia.exceptions.PageError:
            print(f"'{search_input}' page does not exist on Wikipedia.")
        except wikipedia.exceptions.HTTPTimeoutError:
            print("Error: Wikipedia API request timed out. Try again later.")
        except Exception as e:
            print(f"An error occurred: {e}")

main()
