# What is AI
Artificial Intelligence (AI) is the field of building systems that perform tasks which, if a human did them, we would call "intelligent." Below are concise descriptions, approximate first-use year ranges, and representative use cases for each category.

### 1. Early Roots of AI (1950s–1970s)
Foundations: The idea of AI started with early computing pioneers like Alan Turing, who proposed the "Turing Test" in 1950 as a measure of machine intelligence.
For example, systems like expert systems relied on large rule sets to make decisions.
Limitation: These systems couldn’t handle uncertainty or learn from new data — everything had to be explicitly programmed.
  - First-used: 1950s (early AI research) through the 1980s for many deployed expert systems.
  - What: Systems that encode knowledge explicitly as rules (if-then logic) and use an inference engine to make deductions.
  - Use cases: medical diagnosis (early system MYCIN in the 1970s), business rules engines, configuration systems, automated tax/benefits calculators.

### 2. Rise of Machine Learning (1980s–1990s)
This phase marks the shift from hand-coded rules to systems that learn patterns from data using statistical methods.

What changed
- Move away from handcrafted rules toward learning parameters from labeled examples.
- Algorithms became more statistically principled and focused on generalization from finite data.
Key techniques
- Decision trees, k-nearest neighbors, naive Bayes, support vector machines (SVMs).
- Early neural networks (shallow MLPs) reappeared as interest in connectionist models grew.
Drivers
- Better algorithms (SVM kernels, ensemble ideas), increased availability of digital data, and modest improvements in compute.
Typical use cases and properties
- Problems with moderate-sized labeled datasets (tens of thousands of examples).
- Emphasis on feature engineering: domain experts designed the features (e.g., handcrafted text features, engineered image features).


### 3. The Era of Pattern Recognition & Prediction (2000s)
This era centers on applying and scaling machine learning for large-scale pattern recognition and prediction as data volumes exploded.

What changed
- The availability of much larger datasets (web-scale corpora, clickstreams) made data-driven approaches more reliable.
- Ensemble methods and probabilistic models became mainstream for improving accuracy and handling uncertainty.
Key techniques
- Ensemble methods (Random Forests, gradient boosting), probabilistic graphical models (Bayesian networks, CRFs), and improved sequence models.
- Representation learning started maturing (word embeddings, unsupervised feature learning) but often paired with classical models.
Drivers
- Big Data (internet-scale datasets), distributed computing infrastructure (MapReduce/Hadoop), and better tooling for data processing.
Typical use cases and properties
- Recommendation systems, search ranking, fraud detection, large-scale advertising systems.
- Still relied heavily on hand-crafted features or learned embeddings, but models began to incorporate more automated feature learning.


### 4. Deep Learning Revolution (2010s)
Deep learning represents a qualitative shift: end-to-end training of multi-layer neural networks began to outperform traditional pipelines across many domains.

What changed
- Depth (many stacked layers) and representation learning removed much of the need for manual feature engineering.
- Training on GPUs with large datasets enabled models to learn hierarchical features directly from raw data.
Key techniques
- Convolutional Neural Networks (CNNs) for vision, recurrent networks (RNNs/LSTMs) for sequences, and later transformers for attention-based sequence modeling.
- Optimization advances (better initializations, batch normalization, Adam optimizer) and regularization (dropout) improved training stability.
Drivers
- Massive labeled datasets (ImageNet), commodity GPUs and later TPUs, and open-source frameworks (TensorFlow, PyTorch) that made experimentation faster.
Typical use cases and properties
- Breakthroughs in image recognition (ImageNet), speech recognition, machine translation, and reinforcement learning (games and control).
- Models became larger, learned hierarchical features end-to-end, and often required orders of magnitude more compute and data than previous phases.
How to distinguish these phases (quick checklist)
- If the approach depends heavily on engineered features and classical ML models → "Rise of ML" era.
- If the approach scales to huge datasets, uses ensembles or probabilistic models, and emphasizes predictive performance at scale → "Pattern Recognition & Prediction" era.
- If the approach trains deep networks end-to-end on raw data, learns hierarchical representations automatically, and leverages GPUs/TPUs → "Deep Learning Revolution".

### 5. Generative Models & Creativity (Late 2010s–2020s)
This era is characterized by models that generate high-quality new data (text, images, audio) and by architectures and system-level optimizations that made large-scale training practical.

Transformers — why they changed everything
- Self-attention as a primitive: Transformers introduced self-attention, which lets every token in a sequence directly attend to every other token. This flexible connectivity is excellent for capturing long-range dependencies.
- Parallelism and hardware mapping: Unlike recurrent models, transformers compute attention in ways that are highly parallelizable on GPUs/TPUs. This matched advances in hardware and allowed training to scale with model size and dataset size.
- Scaling and emergent capabilities: Transformers scale predictably — larger models trained on more data tend to produce qualitatively new behaviors (few-shot learning, in-context reasoning). This scaling behavior made it practical to invest in massive pre-trained models. --bigger the model, the better they work
- Transfer and versatility: The transformer block is a versatile primitive used for autoregressive generation (GPT), masked-language pretraining (BERT), and encoder-decoder tasks (T5). The same attention machinery was adapted to images, audio, and multimodal tasks.

Practical outcomes
- Pretrained transformers replaced many task-specific pipelines: you can pretrain once at scale and fine-tune (or use few-shot prompting) for many tasks.
- Rapid progress in language modeling, code generation, summarization, translation, dialogue, and multimodal generation.

FlashAttention — fast, memory-efficient attention
FlashAttention is a systems-level optimization (paper by Tri Dao et al.) that implements exact attention more efficiently so larger sequence lengths and batch sizes are possible on the same hardware.

What problem it solves
- Standard attention needs O(n^2) memory in sequence length n (to store attention weights and intermediate matrices). That limits practical sequence lengths and batch sizes.

High-level idea
- Tiled/blocked attention: Compute attention in smaller blocks (tiles) and stream computation so the full attention matrix is never materialized in memory.
- Kernel fusion: Combine matrix multiply, scaling, softmax, and final multiplication into a single fused GPU kernel to reduce memory traffic and increase arithmetic intensity.
- Numerically stable streaming softmax: Maintain running maxima and denominators while processing tiles so the final results match exact attention with good numerical stability.

Why it matters
- Allows exact attention for much longer sequences or larger batches without running out of GPU memory.
- Because the outputs match standard attention, FlashAttention can be used as a drop-in speed/memory optimization in existing transformer models.

Tradeoffs and alternatives
- FlashAttention requires optimized CUDA/metal kernels; it is provided by specialized libraries and integrated into some frameworks.
- Alternatives include sparse attention (Longformer), linearized attention (Performer), and chunked attention (Reformer); these trade some exactness or flexibility for lower asymptotic cost.

Bottom line
- The transformer architecture provided a scalable, general-purpose building block for sequence modeling. System-level optimizations like FlashAttention removed a key practical bottleneck (memory and data movement), enabling training and serving of large and long-context transformer models used in modern LLMs and multimodal systems.


## How to understand LLM (analogy to the brain)
- Neurons, dendrites, synapses — definitions and artificial parallels
  - Neuron (biological): a cell that receives inputs (via dendrites), integrates them in the soma (cell body), and sends outputs along its axon. Neurons communicate at synapses, where neurotransmitters mediate influence.
  - Dendrite: the tree-like input structure of a neuron where many incoming signals are received.
  - Synapse: the junction where one neuron's axon terminal affects another neuron's dendrite or soma; synaptic strength determines how strongly a pre synaptic spike affects the postsynaptic neuron.
  - Artificial parallel: an artificial neuron multiplies inputs by weights (analogous to synaptic strengths), sums them, and applies a nonlinearity. Dendritic computation is only crudely modeled; simple networks aggregate inputs without explicit dendritic branching. Some research models and neuromorphic chips attempt more detailed dendritic or spiking dynamics.
  - Data is store as token


### How to handle different types of data
1. What’s a “Token Space”?
A token is just the smallest chunk of input the model processes.
For text: usually subwords (like “play” + “##ing”).
For images: usually patches (like 16×16 pixel blocks).
For audio: usually small frames or spectrogram slices.
Each token gets mapped into a vector (an embedding), so the model works in a high-dimensional numerical space instead of raw data.
👉 The token space = the collection of all these embedding vectors that represent different input modalities.

2. Text Tokens
Text is split into tokens by a tokenizer (e.g., Byte Pair Encoding, WordPiece).
Each token → an embedding vector (lookup table).

Example:
“The cat sat” → tokens [“The”, “cat”, “sat”].
Each token is mapped to, say, a 768-dim vector.
Unlike bag-of-words (which loses order and context), transformers keep position embeddings and contextualize tokens via self-attention.

3. Image Tokens
Raw pixels are too big, so images are chunked into patches.
Example: Vision Transformer (ViT):
A 224×224 image is split into 16×16 patches → 14×14 = 196 patches.
Each patch is flattened and projected into an embedding vector (same dimension as text embeddings, e.g. 768).
So each image becomes a sequence of patch embeddings = “image tokens.”

4. Audio Tokens
Audio is usually converted into a spectrogram (frequency × time).
Split into small frames or patches.
Each frame is projected into the same embedding space.
So you get a sequence of “audio tokens.”
