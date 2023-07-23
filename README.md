# chatbot-using-pre-trained-model
Chatbot using GODEL pretrained model
<br>
## SETUP
```
pip install -r requirements.txt
git lfs install
git clone https://huggingface.co/microsoft/GODEL-v1_1-base-seq2seq
```


## Fine-tuning
```
import gc
gc.collect()

import torch
torch.cuda.empty_cache()


python GODEL/train.py --model_name_or_path /Proj/GODEL-v1_1-base-seq2seq \
	--dataset_name /Proj/GODEL/examples/dstc9/dstc9_dataset.py \
	--output_dir /Proj/GODEL/test_output \
	--per_device_train_batch_size=4 \
	--per_device_eval_batch_size=4 \
	--max_target_length 512 \
	--max_length 512 \
	--num_train_epochs 1 \
	--save_steps 10000 \
```

## Interaction
```
python EXAMPLE_server.py # start the sever and expose 8080
```


# Start serving frontend page:
```
cd GODEL/html
npm install
npm run serve
```

	--num_beams 5 \
	--exp_name test1 --preprocessing_num_workers 24
