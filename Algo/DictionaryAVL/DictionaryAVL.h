/*Name: Thanakit Yuenyongphisit
  ID:   6309682000
*/
#ifndef DICTIONARY_AVL
#define DICTIONARY_AVL

#include <iostream>
//String manipulator
#include <cctype>
#include <cstring>
#include <string>
//File manipulator library
#include <fstream>
#include <sstream>

//For reduce write "std"
using namespace std;

//Node creation
struct AVLNode
{
    AVLNode* parent;
    AVLNode* left;
    AVLNode* right;
    string word;
    //Constuctor
    AVLNode(string words){
        this->word = words;
        parent = nullptr;
        left = nullptr;
        right = nullptr;
    }
};

class DictionaryAVL{
    public:
        DictionaryAVL();
        AVLNode* root;
        int difference(AVLNode*);
        int count();
        int height();
        //Overlord
        int height(AVLNode*);
        int count(AVLNode*);
        int compareIgnoreCase(string ,string);
        AVLNode* ll_rotate(AVLNode*);
        AVLNode* lr_rotate(AVLNode*);
        AVLNode* rl_rotate(AVLNode*);
        AVLNode* rr_rotate(AVLNode*);
        AVLNode* balance(AVLNode*);
        AVLNode* insertAt(AVLNode* ,AVLNode* ,string);
        void insert(string);
        string show(AVLNode*);
        AVLNode* successor(AVLNode*);
        AVLNode* pop(AVLNode*);
        AVLNode* remove(AVLNode*,AVLNode*,string);
        void remove(string);
        void preOrderPrint();
        void inOrderPrint();
        void postOrderPrint();
        string inOrder(AVLNode*);
        string preOrder(AVLNode*);
        string postOrder(AVLNode*);

        AVLNode* findWord(string);
        AVLNode* find(string);
        AVLNode* findWord(AVLNode*,string);

        AVLNode* findFirstWord();
        AVLNode* findMin();
        AVLNode* findLastWord();
        AVLNode* findMax();

        //file manipulator
        void preOrderWrite(string);
        void readDictionary(string);
        void checkFile(string ,DictionaryAVL*);


};

#endif // IF DECLARED

