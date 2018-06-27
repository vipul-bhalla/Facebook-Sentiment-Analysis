import requests
# preview = []
review = {}
class preview:

    def extractpreview(self, page_id, post_id):

        page_id = page_id

        post_id = post_id

        graph_api_version = 'v2.11'
        access_token = 'EAALOcChZC3PgBAKAE5S5N57gFQDZAqTAYuVhMg0u5FDGaOKrXwvIgGKJWvsEfCGJazssoNKoVEQmZAxbfDK4Ws3Eg2XT7djr3CIdhCdt8uHsYZB67GmQ6yR9HOKKPkL12HISmBUN3C7nWdP60RLMLbwMAFyIoWDTEpZCOFup5vgZDZD'
        url = 'https://graph.facebook.com/{}/{}_{}/?fields=description,name,message,full_picture,caption,from,link'.format(
            graph_api_version, page_id, post_id)


        r = requests.get(url, params={'access_token': access_token})
        data = r.json()
        # print(data)

        if 'error' in data:
            raise Exception(data['error']['message'])

        # preview.append(data['description'])
        # review['description'] = preview
        # print(review)

        for i in data:
            if i != 'id':
                if i == 'from':
                    review[i] = data[i]['name']
                else:
                    review[i] = data[i]

        return review