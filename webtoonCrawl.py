from bs4 import BeautifulSoup
import requests

result = []

def get_naver_webtoon_link(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")

    webtoonCols= soup.find_all('div', {'class': 'col_inner'})

    for col in webtoonCols:
        col2 = col.find_all('li')
        cnt = 0

        for c in col2:
            if cnt == 0:
                day = col.find('span').text # Extract text value of span tag
                cnt += 1

            title = c.find('a', {'title': True})['title'] # Extract the title attribute value of a tag
            webtoon_link = c.find('a', {'href': True})['href'] # Extract the href attribute value of a tag

            webtoon_info = (title, 'https://comic.naver.com' + webtoon_link) # Save the title and url of webtoon in tuple
            result.append(webtoon_info)

        resultCopy = result.copy()

        dic = {'day' : day, 'webtoon_info' : resultCopy}

        cnt = 0

        print(dic)
        result.clear() # Initialize the list variable to store the title and url value of the webtoons of the changed day

if __name__ == "__main__":
    url = 'https://comic.naver.com/webtoon/weekday.nhn'
    get_naver_webtoon_link(url)

