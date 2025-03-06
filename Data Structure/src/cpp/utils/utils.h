#include <string>

namespace returnMethods
{
    struct Result
    {
    public:
        bool Flag;
        std::string log;
    };

    struct Test
    {
    public:
        int a;
    };
}

namespace dataStructures
{
    struct Node
    {
        int index;
        int data;
        Node *next;
    };
}