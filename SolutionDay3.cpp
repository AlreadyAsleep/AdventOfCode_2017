#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

/*
We know the dist from each square will be its root minus 1
so we only need to start from the closest square below our value
and walk our way to the value
*/
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
		//start of the next square
		start++;
		dist++;

		for(int k = 0; k < 4; k++)//each square has 4 sides and since we don't care about direction
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
