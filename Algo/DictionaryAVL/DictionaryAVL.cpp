/*Name: Thanakit Yuenyongphisit
  ID:   6309682000
*/
#include "DictionaryAVL.h"

DictionaryAVL::DictionaryAVL(){
    this->root = nullptr;
}

int DictionaryAVL::height(AVLNode* parent){

    //recursive
    int h = 0;
    if(parent != nullptr){
        int left_height  = height(parent->left);
        int right_height = height(parent->right);
        //compare to find left or right are most
        int most_height = max(left_height , right_height);
        //pick the most
        //+1 because count it self
        h = most_height + 1;
    }
    //base case when input are null will return 0
    return h;
}

// return Negative mean right are heavier
// otherwise Left are Heavier
int DictionaryAVL::difference(AVLNode* parent){
    //Compare left and right child node
    int left_h  = height(parent->left);
    int right_h = height(parent->right);
    //compare result
    int result = left_h - right_h;
    return result;
}

//Rotation
    //LEFT_LEFT
    AVLNode* DictionaryAVL::ll_rotate(AVLNode* parent){
        //to maintain left child node
        AVLNode* temp;
        AVLNode* oldParent;

        oldParent = parent->parent;
        temp = parent->left;

        //parent get right child of left
        parent->left = temp->right;
        //case no child
        if(parent->left != nullptr){
            parent->left->parent = parent;
        }
        //temp become parent and old one go right
        temp->right = parent;
        parent->parent = temp;
        //return new parent
        temp->parent = oldParent;
        return temp;
    }
    //RIGHT_RIGHT
    AVLNode* DictionaryAVL::rr_rotate(AVLNode* parent){
        //maintain right child
        AVLNode* temp;
        AVLNode* oldParent;

        oldParent = parent->parent;
        temp = parent->right;
        //parent get left child of right child
        parent->right = temp->left;
        //case no child
        if(parent->right != nullptr){
            parent->right->parent = parent;
        }

        temp->left = parent;
        parent->parent = temp;

        temp->parent = oldParent;
        return temp;
    }

    AVLNode* DictionaryAVL::lr_rotate(AVLNode* parent){
        //Maintain left child
        AVLNode* temp;
        temp = parent->left;

        //first rotation (to left)
        parent->left = rr_rotate(temp);
        //second rotation (to right) then return
        return ll_rotate(parent);

    }

    AVLNode* DictionaryAVL::rl_rotate(AVLNode* parent){
        //Maintain right child
        AVLNode* temp;
        temp = parent->right;
        //first rotation (to right)
        parent->right = ll_rotate(temp);
        //second rotation (to left) then return
        return rr_rotate(parent);

    }

//Balance function
    AVLNode* DictionaryAVL::balance(AVLNode* temp){
        //factor to check which are heavier
        int factor = difference(temp);
        //LEFT Heavier
        if( factor > 1){
            //LEFT LEFT case
            if(difference(temp->left) > 0)
                temp = ll_rotate(temp);
            //LEFT RIGHT case
            else
                temp = lr_rotate(temp);

        }
        //RIGHT Heavier
        else if (factor < -1){
            //RIGHT RIGHT
            if(difference(temp->right) <= 0)
                temp = rr_rotate(temp);
            //RIGHT LEFT
            else
                temp = rl_rotate(temp);
        }

        //if tree already balance will return with no change
        return temp;

    }
//Manipulation tree
    AVLNode* DictionaryAVL::insertAt( AVLNode* parent ,AVLNode* temp,string word){
        //Base case
        if(temp == nullptr){
            temp = new AVLNode(word);
            temp->parent = parent;
            return temp;
        }
        //input word are less than
        else if( compareIgnoreCase(temp->word , word)>0){

            temp->left = insertAt(temp ,temp->left , word);

            temp = balance(temp);
        }
        //word are more than
        else if( compareIgnoreCase(temp->word,word)<0){

            temp->right = insertAt(temp,temp->right , word);

            temp = balance(temp);
        }
        return temp;
    }

    void DictionaryAVL::insert(string word){
        root = insertAt(nullptr ,root , word);

    }

//String compare
int DictionaryAVL::compareIgnoreCase(string str1 , string str2){
    string temp1 = "";
    string temp2 = "";
    //to lowercase
    for(char& c : str1) {
        temp1 += tolower(c);
    }

    for(char& c : str2) {
        temp2 += tolower(c);
    }

    return temp1.compare(temp2);

}

//Print out
string DictionaryAVL::show(AVLNode* temp){
    return temp->word;
}

string DictionaryAVL::inOrder(AVLNode* temp){
    string str = "";
    //recursive base case
    if(temp == nullptr)
        return str;
    //print lower to highest left first
    str += inOrder(temp->left);
    //print lowest first ( the last at the left then right)
    str += temp->word + " ";
    //right side
    str += inOrder(temp->right);
    return str;
}
void DictionaryAVL::inOrderPrint(){
    cout<<inOrder(root)<<endl;
}

string DictionaryAVL::preOrder(AVLNode* temp){
    string str = "";
    //Recursive base case
    if(temp == nullptr)
        return str;
    //print immedieatly
    str += temp->word + " ";
    //access next node
    str += preOrder(temp->left);
    str += preOrder(temp->right);

    return str;

    }

string DictionaryAVL::postOrder(AVLNode* temp){
    string str = "";
    //Recursive Base case
    if(temp == nullptr)
        return str;
    str += postOrder(temp->left);
    str += postOrder(temp->right);
    str += temp->word + " ";
    return str;
}
//Successor
AVLNode* DictionaryAVL::successor(AVLNode* temp){
    //if have right child
    if(temp->right != nullptr){
        //find least child
        temp = temp->right;

        for(AVLNode* now = temp; now != nullptr; now = now->left){
            temp = now;
        }
        return temp;
    }
    //No right child go parent
    else{
        AVLNode* now = temp;
        AVLNode* p = now->parent;

        //loop till parent are not right child
        while(p != nullptr && now == p->right){
            now = p;
            p = p->parent;
        }
        //return null if no successor
        //otherwise return successor
        return p;
    }


}

AVLNode* DictionaryAVL::remove(AVLNode* p,AVLNode* r,string word){
    //Base case
    if( r == nullptr)
        return r;
    //Word are lesser
    if(compareIgnoreCase(word ,r->word) < 0){
        r->left = remove(r , r->left , word);
        r->parent = p;
    }
    //Word are greater
    if(compareIgnoreCase(word ,r->word) > 0){
        r->right = remove(r , r->right , word);
        r->parent = p;
    }
    //Found removing Node
    else{
        //No child Node
        if(r->left == nullptr && r->right == nullptr){
            delete r;
            return nullptr;
        }
        //One child Node
        else if(root->right == nullptr){
            AVLNode* temp = r->left;
            delete r;
            return temp;
        }
        else if(root->left == nullptr){
            AVLNode* temp = r->right;
            delete r;
            return temp;
        }
        //Node with 2 Child Node
        else{
            //Get successor
            AVLNode* suc = successor(r);
            //Check successor parent
            if(suc->parent != nullptr){
                if(suc->parent != root)
                    suc->parent->left = suc->right;
                else
                    suc->parent->right = suc->right;
            }
            else{
                suc->left = r->left;
            }

            //Copy successor to r
            r->word = suc->word;
            delete suc;
            return r;



        }

    }
    return r;

}
void DictionaryAVL::remove(string word){
    AVLNode* temp = findWord(word);
    this->root = remove(root->parent , root, word);
    root = balance(root);
}


void DictionaryAVL::preOrderPrint(){
    //print from root
    cout<<preOrder(root)<<endl;
    }

void DictionaryAVL::postOrderPrint(){
    //print from root
    cout<<postOrder(root);
    }

int DictionaryAVL::count(AVLNode* temp){
    int size = 0;
    if(temp != nullptr){
        int left_size = count(temp->left) ;
        int right_size = count(temp->right);
        size = left_size + right_size + 1;
    }
    return size;
}
int DictionaryAVL::count(){
    return count(root);
    }

int DictionaryAVL::height(){
    return height(root);
    }

AVLNode* DictionaryAVL::findWord(AVLNode* temp , string word){
    //Recursive base case
    //Not found will return null temp = null mean not found
    if(temp != nullptr){
        //word are greater
        if(compareIgnoreCase(word , temp->word) > 0)
            temp = findWord(temp->right , word);
        //word are lesser
        else if(compareIgnoreCase(word , temp->word) < 0)
            temp = findWord(temp->left , word);

        //founded
        //else if(compareIgnoreCase(word , temp->word) == 0)
         //   return temp;
    }
    return temp;

}
AVLNode* DictionaryAVL::find(string word){
    return findWord(word);

}

AVLNode* DictionaryAVL::findWord(string word){
    return findWord(root , word);
}

AVLNode* DictionaryAVL::findFirstWord(){
    AVLNode* result = nullptr;
    //got left till can't return the last left
    //if root are null then return null
    //result will collect most left before break out of loop
    for(AVLNode* now = root ; now != nullptr ; now = now->left){
        result = now;

    }
    return result;

}
AVLNode* DictionaryAVL::findMin(){
    return findFirstWord();
    }

AVLNode* DictionaryAVL::findLastWord(){
    AVLNode* result = nullptr;
    //find most right Node
    //loop till found most right then break result will collect Node before break
    for(AVLNode* now = root ; now != nullptr ; now = now->right)
        result = now;

    return result;

}

AVLNode* DictionaryAVL::findMax(){
    return findLastWord();
    }

void DictionaryAVL::readDictionary(string files){
    ifstream readFile;
    readFile.open(files);
    string text;

    while(readFile >> text){
        this->insert(text);
    }
    readFile.close();
}

void DictionaryAVL::preOrderWrite(string files){
    ofstream MyWriteFile(files);

    string result = preOrder(root);

    MyWriteFile<<result;

    MyWriteFile.close();


}
void DictionaryAVL::checkFile(string textFileName , DictionaryAVL* tree){
    //Read
    ifstream readFile;
    readFile.open(textFileName);
    string temp = "";
    string text;

    //Write variable (Output)
    ofstream MyWriteFile("output.txt");
    int missingCount = 0;
    int wordCount = 0;
    text = "List of out-of-dictionary words:\n";
    MyWriteFile<<text;

    while(readFile >> text){
        wordCount++;
        temp= "";
        //each char in string
        for(char& c : text) {
            //break if found , " " or .
            if(c == '.' || c == ',')
                continue;
            temp += c;
        }
        //Check are in dict?
        //not found case
        if(tree->findWord(temp) == nullptr){
            missingCount++;
            temp += "\n";
            MyWriteFile<<temp;
        }

    }
    //Conclude Line
    MyWriteFile<<"\n"<<"Number of out-of-dictionary words : ";
    MyWriteFile<<missingCount;
    MyWriteFile<<"\n"<<"Number of words in the file : ";
    MyWriteFile<<wordCount;



    MyWriteFile.close();

    readFile.close();



}






















