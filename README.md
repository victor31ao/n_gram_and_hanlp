# n-gram
## n-gram 的基本概念：

- n-gram 是一種基於統計的方法，用於語言建模和文本分析。
- 一個 n-gram 是文本或語音序列中 n 個連續項的集合。
- 根據 n 的值，可以分為 unigram（n=1）、bigram（n=2）、trigram（n=3）等。

## 為什麼要使用 n-gram：

- n-gram 可以幫助捕捉語言中的局部依賴性。
- 通過統計頻率，可以對語言進行建模，預測下一個詞或詞的序列。
- 在文本分類、語音識別和機器翻譯等應用中廣泛使用。

## n-gram 模型應用範例

1. 語言模型
語言模型的一個重要應用是預測下一個詞。
2. 文本生成
n-gram 的文本生成是一個常見應用。

## 優缺點分析
- 優點：
    - 簡單易用，計算效率高。
    - 對大多數語言任務有良好的效果。
- 缺點：
    - 需要大量的語料來獲取準確的概率分布。
    - 無法捕捉長距依賴性。
    - 隨著 n 的增大，數據稀疏問題嚴重。

# HanLP
HanLP是一個開源的自然語言處理（NLP）庫，專門用於處理中文文本。旨在提供高效、便捷、易於使用的工具來進行各種NLP任務。HanLP 的功能非常豐富，涵蓋了中文NLP的各個方面，以下為幾個主要功能：

1. 分詞：HanLP 提供了高效、準確的中文分詞功能，可以將一段中文文本劃分為單詞序列，這是中文NLP的基礎步驟之一。

2. 詞性標註：在分詞的基礎上，HanLP 可以為每個詞彙標註其詞性（例如名詞、動詞、形容詞等），這對於進一步的語言處理任務非常重要。

3. 命名實體識別（NER）：HanLP 能夠識別出文本中的特定實體，例如人名、地名、組織名等，這對於信息抽取和文本理解非常有用。

4. 依存句法分析：HanLP 提供了句法分析功能，可以解析句子結構，識別詞與詞之間的依存關係，從而理解句子的語法結構。

5. 語料庫及模型：HanLP 包含多種預訓練模型和語料庫，可以方便用戶快速應用到不同的NLP任務中。

6. 文本分類：HanLP 也支持文本分類任務，可以根據文本內容自動歸類到不同的類別中。

7. 情感分析：HanLP 提供了情感分析工具，可以判斷文本的情感傾向，例如正面、負面或中性。

8. 其他工具：此外，HanLP 還包含其他許多實用的NLP工具，如拼音轉換、簡繁體轉換等。

HanLP 的設計注重效率和精度，適合各種規模的應用場景，從學術研究到工業應用。其開源性質使得開發者可以根據需要進行二次開發和定製，並且其社區活躍，經常更新和優化。

總之，HanLP 是一個強大且靈活的中文自然語言處理庫，能夠滿足各種NLP需求，是中文NLP領域中的重要工具之一。
