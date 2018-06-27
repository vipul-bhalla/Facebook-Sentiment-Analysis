import requests

class fetchComments:

    def extract(self, page_id, post_id):

        page_id = page_id

        post_id = post_id

        graph_api_version = 'v2.11'
        access_token = 'xxxxxxxxxx'

        url = 'https://graph.facebook.com/{}/{}_{}/comments'.format(graph_api_version, page_id, post_id)

        comments = []

        r = requests.get(url, params={'access_token': access_token})
        while True:
            data = r.json()

            # catch errors returned by the Graph API
            if 'error' in data:
                raise Exception(data['error']['message'])

            # append the text of each comment into the comments list
            for comment in data['data']:
                # remove line breaks in each comment
                text = comment['message'].replace('\n', ' ')
                comments.append(text)

            # print('got {} comments'.format(len(data['data'])))

            # check if there are more comments
            if 'paging' in data and 'next' in data['paging']:
                r = requests.get(data['paging']['next'])
            else:
                break

        # save the comments to a file
        with open('scrape_data.txt', 'wb+') as f:
            for comment in comments:
                f.write(comment.encode("utf-8") + "\n".encode("ascii"))
