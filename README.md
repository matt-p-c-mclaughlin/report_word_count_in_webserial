# report_word_count_in_webserial

A project to scrape a webpage, count how many times a certain word is used, locate the link for the next chapter, traverse all available chapters, and return a detailed report on the word count.

Currently set up to count "smirk" in [All Jobs and Classes! I Just Wanted One Skill, Not Them All!](https://www.royalroad.com/fiction/130987/all-jobs-and-classes-i-just-wanted-one-skill-not), but can easily be updated. Note- I have a hotfix in that stops counting when it hits a page with the author's username, so if updating the script make sure to hit that too. 

## Key concepts learned

Scraping with BeautifulSoup, generating reports by redirecting stdout, ...