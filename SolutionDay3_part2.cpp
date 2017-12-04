#include <cmath>
#include <iostream>
#include <vector>
using namespace std;


typedef struct Matrix
{
public:
	vector< vector<int> > mat;
	Matrix(int size)
	{
		for(int i = 0; i < size; i++)
		{
			vector<int> temp(size);
			mat.push_back(temp);
		}
	}

	void print()
	{
		for(int i = 0; i < mat.size(); i++)
		{
			for(int j = 0; j < mat.size(); j++)
			{
				cout << mat[i][j] << " ";
			}
			cout << endl;
		}
		cout << endl;
	}

	void fillWithAdjSum(int bound)
	{
		int temp = 0;
		int x = mat.size() / 2;
		int y = x;
		int counter = 1;
		mat[x][y] = 1;
		while(temp < bound && x < mat.size() && y < mat.size()) 
		{
			for(int i = 0; i < counter; i++)
			{
				x++;
				fillMemberWithAdjSum(x,y,temp);
			}
			for(int i = 0; i < counter; i++)
			{
				y--;
				fillMemberWithAdjSum(x,y,temp);
			}
			counter++;
			for(int i = 0; i < counter; i++)
			{
				x--;
				fillMemberWithAdjSum(x,y,temp);
			}
			for(int i = 0; i < counter; i++)
			{
				y++;
				fillMemberWithAdjSum(x,y,temp);
			}
			counter++;
		}
	}

	void fillMemberWithAdjSum(int x, int y, int &t)
	{
		t = mat[x-1][y-1] + mat[x-1][y] + mat[x-1][y+1] + 
			mat[x][y-1] + mat[x][y+1] + mat[x+1][y-1] + mat[x+1][y]
			+ mat[x+1][y+1];
		mat[x][y] = t;

	}
};

int main(int charc, char* argv[])
{
	Matrix matrix(20);
	matrix.print();
	matrix.fillWithAdjSum(265149);
	matrix.print();
	return 0;
}
