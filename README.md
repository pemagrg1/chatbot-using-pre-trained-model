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

## FOLDER INFORMATION
1. SMF
[Folder](SMF)

This is the folder where we store files relating to our fine-tuned model, including datasets, fine-tuned models with checkpoints, server file. 

3. SMF/ckpt
[Folder](SMF/ckpt/)

This is the folder where checkpoints are stored(It is too large for uploading in Github). 

4. SMF/json_data
[Folder](SMF/json_data/)

This is the folder where datasets are stored.
new_train_data.jsonl and new_test_data.jsonl are the datasets with knowledge. 
new_train_data.jsonl and new_test_data.jsonl are the datasets without knowledge. 

5. SMF/analysis.py
[File](SMF/analysis.py)

This is the file for analysis. 

6. SMF/SMF_dataset.py
[File](SMF/SMF_dataset.py)

This is the file for loading the dataset used in fine-tuning phases.

7. SMF/SMF_server.py
[File](SMF/SMF_server.py)

This is the file for running the server using our fine-tuned model.

## SETUP
[GODEL](https://github.com/microsoft/GODEL.git)
1. Clone the GODEL repo
```
$ git clone https://github.com/microsoft/GODEL.git
```
2. Install the requirements
```
pip install -r GODEL/requirements.txt
```
3. Download the pretrained model
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

# Interact with the Chatbot
1. Open a terminal and the following code:
```
cd GODEL/html
npm install
npm run serve
```
2. Open another terminal and run the SMF_server.py file
```
python SMF/SMF_server.py # start the sever and expose 8080
```
