#include <iostream>
#include "utils/utils.h"

using namespace std;
using namespace returnMethods;

Result test()
{
    Result values;
    values.Flag = true;
    values.log = "This is log";
    return values;
}

int main()
{
    Result data = test();
    cout << "Flag " << data.Flag << endl;
    cout << "Logs " << data.log << endl;
    return 0;
}