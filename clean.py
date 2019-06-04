def clean_soup(soup):
    for script in soup(["script", "style"]):
        script.decompose()
    main_text = soup.get_text()
    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in main_text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)

    return(text)
