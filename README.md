# chatbot-using-pre-trained-model
The "Stuttgart Music Festival Chatbot" is a goal-directed chatbot designed to enhance the experience and engagement of attendees and potential visitors to the music festivals in Stuttgart. The chatbot is built using the GODEL model, a Transformer-based encoder-decoder model that is fine-tuned using dialog context and external knowledge to generate suitable responses.<br>

#### Features
The chatbot's main functionalities include providing general information about two music festivals (Rottweiler Jazz Festival and the SWR Summer Festival), such as festival names, programs, music genres, and participating bands. It also offers organization information like dates, locations, venues, and event schedules. Users can inquire about ticketing details for specific festivals, including how to buy tickets, ticket prices, student discounts, and booking information.

#### Implementation
The implementation involved manually creating 60 dialog data, which was then converted to the GODEL model's data format. The model was fine-tuned with 40 training data and evaluated using 20 testing data. Two setups were evaluated: one with knowledge data and one without knowledge data. The evaluation metrics used include BLEU (Bilingual Evaluation Understudy) and ROUGE (Recall-Oriented Understudy for Gisting Evaluation) scores.

#### Results
The results showed that the model using external knowledge performed better in generating dialogue responses. However, there were some challenges, including the need for GPU support, difficulties in controlling dataset quality, and the risk of producing parroted or redundant responses.

#### Future Work
Future work includes expanding the training data for dialogue, improving dataset quality, and adding additional features like Navigation Support, Real-Time Updates, and a Recommendations system based on user preferences.
<br>

## SETUP
[GODEL](https://github.com/microsoft/GODEL.git)
1. Install the requirements
```
pip install -r GODEL/requirements.txt
```
2. Download the pretrained model
```
$ git lfs install
$ git clone https://huggingface.co/microsoft/GODEL-v1_1-base-seq2seq
```

## Fine-tuning
```
python train.py --model_name_or_path GODEL-v1_1-base-seq2seq \
	--dataset_name SMF/SMF_dataset.py \
	--output_dir SMF/ckpt \
	--per_device_train_batch_size=2 \
	--per_device_eval_batch_size=4 \
	--max_target_length 128 \
	--max_length 256 \
	--num_train_epochs 50 \
	--save_steps 10000 \
	--num_beams 5 \
	--exp_name wow-test \
	--preprocessing_num_workers 24 \
	--save_every_checkpoint 
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
