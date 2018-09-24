#include <bits/stdc++.h>
#include <string>
using namespace std;

int g_x = 9;
const int g_y(2);
static int g_z;
void doSomething()
{
    ::g_x = 3;									//use :: to acces vaue of gloabl variable
    // ::g_y = 10;    							not possible to read only
    // std::cout << "g_y  " << g_y << "\n";      constant value
}
 
int main()
{
	std::string name("Vishal");
	cout << name;
	int g_x = 11;
	cout << "g_x  " << ::g_x << "\n";
	cout << "g_z  " << g_z << "\n";
	int g_z = 100;
	cout << "g_z  " << g_z << "\n";
    doSomething();
 	cout << "g_x  " << g_x << "\n";
    ::g_x = 5;
    // std::cout << "g_y1  " << g_y << "\n";
 	cout << "g_x  " << ::g_x << "\n";
    return 0;
}