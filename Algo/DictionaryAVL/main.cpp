/*Name: Thanakit Yuenyongphisit
  ID:   6309682000
*/
#include"DictionaryAVL.h"


int main(int argc, char *argv[]) {
 DictionaryAVL *tree = new DictionaryAVL();
 // insert data from the input file into the tree
 tree->readDictionary("dict.txt");
 cout << "Number of words = " << tree->count() << endl;
 tree->inOrderPrint();
 cout << "First Word: "<< tree->show(tree->findMin())<<endl;
 cout << "Last Word: "<< tree->show(tree->findMax())<<endl;
 tree->preOrderWrite("preorderDict.txt");
 AVLNode * temp = tree->find("much");
 if (temp != NULL) {
 cout << "Find: "<<tree->show(temp)<<endl;
 }
 tree->remove("time");
 tree->insert("most");
 tree->insert("time");
 tree->preOrderWrite("outputRemoveInsert.txt");
  cout << "Number of words = " << tree->count() << endl;
 cout << "Tree height = " << tree->height() << endl;
 //Last test case
 tree->checkFile("sample.txt" , tree);
 delete tree;


 return EXIT_SUCCESS;
}
