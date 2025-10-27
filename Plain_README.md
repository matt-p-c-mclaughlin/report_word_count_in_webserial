# report_word_count_in_webserial

A project to scrape a webpage, count how many times a certain word is used, locate the link for the next chapter, traverse all available chapters, and return a detailed report on the word count.

Currently set up to count "smirk" in [All Jobs and Classes! I Just Wanted One Skill, Not Them All!](https://www.royalroad.com/fiction/130987/all-jobs-and-classes-i-just-wanted-one-skill-not), but can easily be updated. Note- I have a hotfix in that stops counting when it hits a page with the author's username, so if updating the script make sure to hit that too. 

#### Key concepts learned

Scraping with BeautifulSoup, generating reports by redirecting stdout, manipulating text and Markdown files, ...

### TODO / Backlog
- [ ] Remove hotfix that checks against author name
  - Option 1: grab the author name early, when grabbing "possible Next Chapter link", compare against author name
  - Option 2: When grabbing "possible Next Chapter link", grab it's text and look for "Next".
  - Neither should slow the code too much. What was slowing things down is when I grabbed every "a" button in the page and checked it's text for "Next". From testing, the only time the second index "a" button will not have text of "Next" will be on the last chapter, because that will be the Author link. **Use Option 2**
- [ ] Allow user input to input the *Chapter 1 link* and the *search keyword*
- [ ] Format the Chapter Count List into a table or something more readable (may not play well with collapsing dropdown)
