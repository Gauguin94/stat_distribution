from link_dist import*

distn_list = ['B','NB','G','P','r','X_2','Beta','N']

if __name__ == "__main__":
    select_dist = linkToDist()
    select_dist.switch('B') # or u can use "select_dist.switch(distn_list[0])"
