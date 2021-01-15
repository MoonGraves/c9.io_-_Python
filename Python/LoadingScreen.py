import time
from tqdm import tqdm

for _ in tqdm(range(100),
        desc="Loading...",
        ascii=False, ncols= 95):
    
    #Tässä on määritetty 2s
    time.sleep(0.02)
  
print("Loading success")

#########
#Output shortly::
#Loading...:   0%|                                                      | 0/100 [00:00<?, ?it/
#Loading...:  10%|████▌                                        | 10/100 [00:00<00:01, 49.56it/
#Loading...:  90%|████████████████████████████████████████▌    | 90/100 [00:01<00:00, 49.47it/
#Loading...: 100%|████████████████████████████████████████████| 100/100 [00:02<00:00, 49.48it/s]
#Loading Scucess
#
#
#
