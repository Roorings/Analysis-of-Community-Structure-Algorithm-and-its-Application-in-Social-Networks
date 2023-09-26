G = nx.read_edgelist('email-Eu-core.txt', comments='#', create_using=nx.Graph(), delimiter=' ',  nodetype=int, encoding='utf-8')
txt = np.loadtxt('email-Eu-core-department-labels.txt')
membershipGT = []
for i in range(len(txt)):
    membershipGT.append(txt[i][1])

communitiesFG = greedy_modularity_communities(G, weight=None, resolution=1, n_communities=1)
lstFG = [list(x) for x in communitiesFG]
membershipFG = network_community(lstFG,G)

imfb = Infomap("-k --include-self-links --clu --ftree -d --directed")
imfb.read_file("email-Eu-core.txt")
imfb.run()
print(f"Found {imfb.num_top_modules} modules with codelength: {imfb.codelength}")
membershipIN = []
for i in range(len(imfb.get_modules())):
    membershipIN.append(imfb.get_modules()[i])

print(compare_communities(membershipIN, membershipGT, method='nmi', remove_none=False))
print(compare_communities(membershipFG, membershipGT, method='nmi', remove_none=False))
                    