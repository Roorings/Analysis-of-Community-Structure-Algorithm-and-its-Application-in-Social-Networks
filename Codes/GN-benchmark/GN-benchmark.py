lstin = []
lstfg = []
for j in range(1,15):
    pin = 0.38 - 0.02 * j
    pout = 4 / 600 + 4 / 600 * j
    avein = 0
    avefg = 0
    for k in range(20):
        G = nx.random_partition_graph([50, 50, 50, 50], pin, pout, directed = False)
        partition = G.graph["partition"]
        lstRP = [list(x) for x in partition]
        membershipRP = network_community(lstRP,G)
        communitiesFG = greedy_modularity_communities(G, weight=None, resolution=1, n_communities=1)
        lstFG = [list(x) for x in communitiesFG]
        membershipFG = network_community(lstFG,G)
        origin_edges = nx.to_edgelist(G)
        new_list = []
        for edge_i in range(0,len(origin_edges)):
            node_dict = list(origin_edges)[edge_i]
            new_list.append([node_dict[0],node_dict[1]])
        g = Graph(new_list)  
        h1 = g.community_infomap()
        community_list_new = list(h1)
        list(community_list_new).remove(community_list_new[0])  
        membershipINFOMAP = network_community(community_list_new,G)
        avein = avein + compare_communities(membershipINFOMAP, membershipRP, method='nmi', remove_none=False)
        avefg = avefg + compare_communities(membershipFG, membershipRP, method='nmi', remove_none=False)
    print('end')
    print(avefg/20)
    print(avein/20)
    lstfg.append(avefg/20)
    lstin.append(avein/20)
