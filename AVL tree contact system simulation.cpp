#include <iostream>
#include <vector>
#include <string>
using namespace std;
template <typename T>
struct node {
	T data;
	node* left = nullptr; 
	node* right = nullptr;
	int height = 1;

	node(T value)
		: data(value), left(nullptr), right(nullptr), height(1) {}
};
struct Contact {
	string name;
	string phoneNumber;

	Contact(const string& _name, const string& _phoneNumber)
		: name(_name), phoneNumber(_phoneNumber) {}

	bool operator<(const Contact& other){
		return name < other.name;
	}

	bool operator>(const Contact& other){
		return name > other.name;
	}

	bool operator==(const Contact& other){
		return name == other.name;
	}

	friend ostream& operator<<(ostream& os, const Contact& contact) {
		os << contact.name << ": " << contact.phoneNumber;
		return os;
	}
};

template <typename T>
class AVL {
private:
	node<T>* root;
	node<T>* findMin(node<T>* tree) {
		if (tree == nullptr) return nullptr;
		while (tree->left != nullptr) {
			tree = tree->left;
		}
		return tree;
	}
	

	int getheight(node<T>* subtree) {
		if (subtree == nullptr) return 0;
		return subtree->height;
	}


	int balancefactor(node<T>* subtree) {
		if (subtree == nullptr) return 0;
		return getheight(subtree->left) - getheight(subtree->right);
	}


	node<T>* rotateRight(node<T>* y) {
		node<T>* x = y->left;
		node<T>* T2 = (x != nullptr) ? x->right : nullptr;

		if (x != nullptr) x->right = y;

		y->left = T2;

		y->height = max(getheight(y->left), getheight(y->right)) + 1;
		if (x != nullptr) x->height = max(getheight(x->left), getheight(x->right)) + 1;

		return x;
	}


	node<T>* rotateLeft(node<T>* y) {
		node<T>* x = y->right;
		node<T>* T2 = (x != nullptr) ? x->left : nullptr;
		if (x != nullptr) x->left = y;
		y->right = T2;

		y->height = max(getheight(y->left), getheight(y->right)) + 1;
		if(x != nullptr)x->height = max(getheight(x->left), getheight(x->right)) + 1;

		return x;
	}


	node<T>* insertnode(node<T>* tree, T value) {
		if (tree == nullptr) return new node<T>(value);

		if (value < tree->data) {
			tree->left = insertnode(tree->left, value);
		}
		else if (value > tree->data) {
			tree->right = insertnode(tree->right, value);
		}
		else {
			return tree; 
		}


		tree->height = max(getheight(tree->left), getheight(tree->right)) + 1;

		int balance = balancefactor(tree);

		if (balance > 1 && value < tree->left->data)
			return rotateRight(tree);

		if (balance < -1 && value > tree->right->data)
			return rotateLeft(tree);

		if (balance > 1 && value > tree->left->data) {
			tree->left = rotateLeft(tree->left);
			return rotateRight(tree);
		}

		if (balance < -1 && value < tree->right->data) {
			tree->right = rotateRight(tree->right);
			return rotateLeft(tree);
		}

		return tree;
	}

	node<T>* deletenode(node<T>* tree, T value) {
		if (tree == nullptr) return tree;

		if (value < tree->data) tree->left = deletenode(tree->left, value);

		else if (value > tree->data) tree->right = deletenode(tree->right, value);

		else {
			if (tree->left == nullptr) {
				node<T>* temp = tree->right;
				delete tree;
				return temp;
			}
			else if (tree->right == nullptr) {
				node<T>* temp = tree->left;

				delete tree;
				return temp;
			}
			node<T>* successor = findMin(tree->right);
			tree->data = successor->data;
			tree->right = deletenode(tree->right, successor->data);
		}
		tree->height = max(getheight(tree->right), getheight(tree->left)) + 1;

		int balance = balancefactor(tree);

		if (balance > 1 && value < tree->left->data)
			return rotateRight(tree);

		if (balance < -1 && value > tree->right->data)
			return rotateLeft(tree);

		if (balance > 1 && value > tree->left->data) {
			tree->left = rotateLeft(tree->left);
			return rotateRight(tree);
		}

		if (balance < -1 && value < tree->right->data) {
			tree->right = rotateRight(tree->right);
			return rotateLeft(tree);
		}
		return tree;
	}


	bool searchnode(node<T>* tree, T value) {
		if (tree == nullptr) {
			return false;
		}
		else if (value < tree->data) {
			return searchnode(tree->left, value);
		}
		else if (value > tree->data) {
			return searchnode(tree->right, value);
		}
		else {
			return true;
		}
	}
	void print(node<T>* tree) {
		if (tree == nullptr) return;
		print(tree->left);
		cout << tree->data << " ";
		print(tree->right);
	}

public:
	AVL() {
		root = nullptr;
	}
	void insert(T value) {
		root = insertnode(root,value);
	}
	void deletes(T value) {
		root = deletenode(root,value);
	}
	void inorder() {
		print(root);
	}
	bool search(T value) {
		return searchnode(root, value);
	}
};

int main() {
	AVL<Contact> contacts;
	int choice;
	string name, phoneNumber;

	while (true) {
		cout << "========== Contact Menu ==========" << endl;
		cout << "1. Add Contact" << endl;
		cout << "2. Search Contact" << endl;
		cout << "3. Delete Contact" << endl;
		cout << "4. Display Contact List" << endl;
		cout << "5. Exit" << endl;
		cout << "Enter your choice: ";
		cin >> choice;

		switch (choice) {
		case 1: {
			cout << "Enter contact name: ";
			cin >> name;
			cout << "Enter contact phone number: ";
			cin >> phoneNumber;

			contacts.insert(Contact(name, phoneNumber));
			cout << "Contact added successfully." << endl;
			break;
		}
		case 2: {
			cout << "Enter contact name to search: ";
			cin >> name;

			if (contacts.search(Contact(name, ""))) {
				cout << "Contact found: " << name << endl;
			}
			else {
				cout << "Contact not found: " << name << endl;
			}
			break;
		}
		case 3: {
			cout << "Enter contact name to delete: ";
			cin >> name;

			contacts.deletes(Contact(name, ""));
			cout << "Contact deleted successfully." << endl;
			break;
		}
		case 4: {
			cout << "Contact List: ";
			contacts.inorder();
			cout << endl;
			break;
		}
		case 5: {
			cout << "Exiting program..." << endl;
			return 0;
		}
		default: {
			cout << "Invalid choice. Please try again." << endl;
			break;
		}
		}
		cout << endl;
	}
}
