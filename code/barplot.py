import matplotlib.pyplot as plt
import Insertion as i
import Selection as s
import Bubble as b
import Mergesort as m
import quicksort as ql
import Quicksort_median as qm
import Heapsort as h

# plotting run_time complexities
y = [s.run_time_s, b.run_time_b, i.run_time_i, m.run_time_m, ql.run_time_ql, qm.run_time_qm, h.run_time_h]
x = ['selection', 'bubble', 'insertion', 'merge', 'quick', 'quick_median', 'heap']
plt.title('Run time complexities for all sorting techniques')
plt.bar(x, y)
plt.xlabel('sorting technique')
plt.ylabel('Runtime')
plt.show()
plt.savefig('./runtimes.png',dpi=150)