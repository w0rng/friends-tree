import requests
import networkx as nx
import matplotlib.pyplot as plt

START_ID = 12341234
COUNT_GET_FRIENDS = 7
DEPTH = 4


def get_firiends(_id):
    resp = requests.get(
        "https://api.vk.com/method/friends.get?user_id=%s&count=%s&v=5.73"
        % (_id, COUNT_GET_FRIENDS)).json()
    print(resp)
    return resp['response']['items']


def main():
    frinds = []
    parsed_data = [START_ID]
    old_data = []
    lauer = 0

    while lauer < DEPTH:
        for _id in parsed_data[::]:
            get_friend = get_firiends(_id)
            if get_friend:
                for friend in get_friend:
                    temp = (_id, friend, 1)
                    frinds.append(temp)
                    if friend not in old_data:
                        parsed_data.append(friend)
                old_data.append(_id)
                del parsed_data[parsed_data.index(_id)]
        lauer += 1

    graph = nx.Graph()
    graph.add_weighted_edges_from(frinds)
    nx.draw_networkx(graph, with_labels=False, node_size=20, node_color="red")
    plt.show(block=False)
    plt.savefig("Graph.png", format="PNG")


if __name__ == '__main__':
    main()
