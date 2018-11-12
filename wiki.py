# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 13:33:15 2018

@author: mnunes
"""

import wikipedia


tree_of_topics=[]

max_length=10
def get_topics(keyword,list_of_topics,max_length):
    if len(list_of_topics) < max_length:
        wiki_res=wikipedia.search(keyword)
        for wiki_res_i in wiki_res:
            if not wiki_res_i in list_of_topics and len(list_of_topics) < max_length:
                list_of_topics.append(wiki_res_i)
                k=len(list_of_topics)
                list_of_topics=get_topics(wiki_res_i,list_of_topics,max_length)

                if len(list_of_topics)==k:
                    break
   
        

    return list_of_topics
        


top_search='Pokemon'

tree_of_topics=get_topics(top_search,tree_of_topics,max_length)
print()
print("found the folloiwng items with no more than "+str(max_length)+" in list")
print()

print(tree_of_topics)