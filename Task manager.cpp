#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <algorithm>
#include <ctime>
#include <chrono>
#include <iomanip>
using namespace std;

template <typename T>
class PriorityQueue {
private:
	vector<T>heap;
	int leftChild(int i) {
		return 2 * i + 1;
	}
	int rightChild(int i) {
		return 2 * i + 2;
	}
	int parent(int i) {
		return (i - 1) / 2;
	}
	void siftup(int i) {
		while (i != 0 && heap[i] > heap[parent(i)]) {
			std::swap(heap[i], heap[parent(i)]);
			i = parent(i);
		}
	}
	void siftdown(int i) {
		int largest = i;
		if (leftChild(i) < heap.size() && heap[leftChild(i)] > heap[largest]) {
			largest = leftChild(i);
		}

		if (rightChild(i) < heap.size() && heap[rightChild(i)] > heap[largest]) {
			largest = rightChild(i);
		}

		if (largest != i) {
			swap(heap[i], heap[largest]);
			siftdown(largest);
		}
	}
public:
	size_t size() {
		return heap.size();
	}
	bool empty() {
		return heap.size() == 0;
	}
	T top() {
		if (empty()) {
			throw runtime_error("queue is empty");
		}
		return heap[0];
	}
	void push(T value) {
		heap.push_back(value);
		siftup(int(heap.size() - 1));
	}
	T extractMax() {
		if (empty()) {
			throw runtime_error("queue is empty");
		}
		T temp = heap[0];
		swap(heap[0], heap[heap.size() - 1]);
		heap.pop_back();
		siftdown(0);
		return temp;
	}
};
string get_time() {
	time_t currentTime = std::time(nullptr);
	char timeString[100];
	strftime(timeString, sizeof(timeString), "%Y-%m-%d", std::localtime(&currentTime));
	return timeString;
}
struct to_do {
	string created, due, task, priority, status, comment;
	to_do(string t, string d = "", string p = "", string c = "", string s = "Not started") :
		due(get_time()), task(t), priority(p), status(s), comment(c), created(get_time()){
		for (int i = 0;i < d.size();i++) {
			due[i] = d[i];
		}
	}
	bool operator<(const to_do& other) const {
		std::string priorityOrder[] = { "High", "Medium", "Low" };

		int thisPriorityIndex = -1;
		int otherPriorityIndex = -1;

		for (int i = 0; i < 3; ++i) {
			if (priority == priorityOrder[i]) {
				thisPriorityIndex = i;
			}
			if (other.priority == priorityOrder[i]) {
				otherPriorityIndex = i;
			}
		}
		return thisPriorityIndex < otherPriorityIndex;
	}
	friend std::ostream& operator<<(std::ostream& os, const to_do& td) {
		os << "Task: " << td.task << setw(5) << "Status: " << td.status <<
			setw(5) << "Due date: " << td.due << setw(5) << "Priority: " << td.priority;
			return os;
	}
 };
