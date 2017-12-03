#include <iostream>
#include <cmath>
#include <vector>
using namespace std;


int findClosestSquareFloor(int i)
{
	int root_i = (int)floor(sqrt(i));
	int temp = root_i * root_i;
	return temp;
}

int distanceTo1(int num)
{
	int start = findClosestSquareFloor(num);
	int dist = (int)sqrt(start) - 1;
	if(start != num)
	{
		start++;
		dist++;

		for(int k = 0; k < 4; k++)
		{
			for(int i = 0; i < (int)sqrt(start) / 2 && start != num; i++)
			{
				start++;
				dist--;
			}
			for(int i = (int)sqrt(start) / 2; i < (int)sqrt(start) && start != num; i++)
			{
				start++;
				dist++;
			}
		}

	}
	return dist;
}

int main(int charc, char* argv[])
{
	int num;
	cin >> num;
	cout << distanceTo1(num);
	return 0;
}
