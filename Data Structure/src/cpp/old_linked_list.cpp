#include <iostream>
#include <string>
#include "utils/utils.h"

using namespace std;
using namespace returnMethods;

class Node
{
public:
    std::string data;
    int index;
    Node *next;

    Node()
    {
        index = 0;
        data = "";
        Node *next = NULL;
    }

    Node(int index, string data)
    {
        index = index;
        data = data;
    }
};

class LinkedList
{
public:
    Node *head;

private:
    bool nodeExist(int index)
    // Todo: Store this index in hashmap
    {
        Node *iterator = head;
        while (iterator != NULL)
        {
            if (iterator->index == index)
            {
                return true;
            }
            iterator = iterator->next;
        }
        return false;
    }

public:
    bool addNode(Node *node)
    {
        if (nodeExist(node->index))
        {
            // cout << "Node with " << node->index << " already exists." << endl;
            return false;
        }

        node->next = head;
        head = node;
        // cout << "Node added in linked list" << endl;
        return true;
    }

    void print()
    {
        if (head == NULL)
        {
            cout << "Linked List is Empty." << endl;
        }
        else
        {
            Node *iterator = head;
            while (iterator != NULL)
            {
                cout << "[ " << iterator->index << " = " << iterator->data << " ]" << endl;
                cout << "   ***   " << endl;
                cout << "    |    " << endl;
                cout << "    |    " << endl;
                cout << "   ***   " << endl;
                iterator = iterator->next;
            }
            cout << "\tNULL" << endl
                 << endl;
        }
    }

    void print_recursive(Node *node)
    {
        if (node != NULL)
        {
            cout << "[ " << node->index << " = " << node->data << " ]" << endl;
            cout << "   ***   " << endl;
            cout << "    |    " << endl;
            cout << "    |    " << endl;
            cout << "   ***   " << endl;
            print_recursive(node->next);
        }
    }

    void print_reverse(Node *node)
    {
        if (node != NULL)
        {
            print_reverse(node->next);
            cout << "[ " << node->index << " = " << node->data << " ]" << endl;
            cout << "   ***   " << endl;
            cout << "    |    " << endl;
            cout << "    |    " << endl;
            cout << "   ***   " << endl;
        }
    }
};

int main()
{
    LinkedList LL;
    int option, index;
    string data;

    do
    {
        cout << "Enter your choice" << endl;
        cout << "Choose the operation you want to do on the list" << endl;
        cout << "Press 1 to add node in the last of the list:" << endl;
        cout << "Press 2 to add node in the front of the list:" << endl;
        cout << "Press 3 to insert node in between the list:" << endl;
        cout << "Press 4 to delete node in the list:" << endl;
        cout << "Press 5 to update data of node in the list:" << endl;
        cout << "Press 6 to print the list:" << endl;
        cout << "Press 7 to clear screen in terminal:" << endl;
        cout << "Press 0 to exit from the loop:" << endl;

        cin >> option;

        Node *node = new Node();

        switch (option)
        {
        case 0:
            cout << "" << endl;
            break;

        case 1:
            cout << "Enter key and data of the node to be appended " << endl;
            cin >> index;
            cin >> data;
            node->index = index;
            node->data = data;
            bool result = LL.addNode(node);
            if (result == true)
            {
                cout << "Node added in linked list" << endl;
            }
            else
            {
                cout << "Node with " << node->index << " already exists." << endl;
            }
            break;

        case 2:
            LL.print();
            break;
        case 3:
            system("cls");
            break;

        default:
            cout << "Wrong option." << endl;
            break;
        }

    } while (option != 0);
    return 0;
}
