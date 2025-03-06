#include <iostream>
#include "utils/utils.h"

using namespace std;
using namespace dataStructures;

class LinkedList
{
public:
    Node *head;

private:
    bool nodeExist(int index)
    {
        if (is_empty())
        {
            return false;
        }
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

    bool is_empty()
    {
        if (head == NULL)
        {
            return true;
        }
        return false;
    }

public:
    bool add_node(Node *node)
    {
        cout << "Adding Node" << endl;
        node->next = head;
        head = node;
        return true;
    }

    void print()
    {
        if (is_empty())
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
    LL.print();

    Node *node = new Node();
    node->index = 1;
    node->data = 10;
    LL.add_node(node);
    LL.print();

    Node *node2 = new Node();
    node2->index = 2;
    node2->data = 20;
    LL.add_node(node2);
    LL.print();

    return 0;
}