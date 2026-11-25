import math
import csv

# Illustrative categories and assumed action likelihoods, not fitted player data.
PRIOR={'strong':0.2,'medium':0.5,'weak':0.3}
LIKELIHOOD={'bet':{'strong':0.8,'medium':0.4,'weak':0.2},'check':{'strong':0.2,'medium':0.6,'weak':0.8}}
EQUITY={'strong':0.15,'medium':0.5,'weak':0.8}

def update(prior,action):
    weights={h:p*LIKELIHOOD[action][h] for h,p in prior.items()}
    total=sum(weights.values())
    if total<=0: raise ValueError('Impossible observation')
    return {h:w/total for h,w in weights.items()}

def equity(posterior): return sum(p*EQUITY[h] for h,p in posterior.items())
def call_ev(q,pot,cost): return q*pot-(1-q)*cost

def main():
    posterior=update(PRIOR,'bet')
    print('Posterior:',posterior,'Equity:',equity(posterior))
    with open('results.csv','w',newline='') as f:
        w=csv.writer(f); w.writerow(['weak_bet_likelihood','posterior_strong','posterior_medium','posterior_weak','equity','call_ev'])
        for i in range(1,10):
            LIKELIHOOD['bet']['weak']=i/10; LIKELIHOOD['check']['weak']=1-i/10
            p=update(PRIOR,'bet'); q=equity(p); w.writerow([i/10,*p.values(),q,call_ev(q,100,50)])
    LIKELIHOOD['bet']['weak']=0.2; LIKELIHOOD['check']['weak']=0.8
if __name__=='__main__': main()
