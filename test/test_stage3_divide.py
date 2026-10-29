import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.stage3_divide_conquer import divide_graph


class TestDivideGraph(unittest.TestCase):

    def setUp(self):
        """Khoi tao cac bo du lieu kiem thu tieu chuan."""
        # Bo du lieu mau 4 diem (muc 5.1 README): Ha Noi, Ha Long, Ninh Binh, Sa Pa
        self.n_sample = 4
        self.locations_sample = ["Ha Noi", "Ha Long", "Ninh Binh", "Sa Pa"]
        self.fame_sample = [0, 8, 7, 9]
        self.budget_sample = 1500000.0
        self.cost_matrix_sample = [
            [0.0, 320000.0, 180000.0, 640000.0],
            [320000.0, 0.0, 400000.0, 900000.0],
            [180000.0, 400000.0, 0.0, 760000.0],
            [640000.0, 900000.0, 760000.0, 0.0]
        ]

        # Bo du lieu 6 diem (N chan)
        self.n_6 = 6
        self.fame_6 = [0, 5, 8, 3, 9, 6]
        self.budget_6 = 2000000.0
        self.cost_matrix_6 = [
            [0, 10, 20, 15, 30, 25],
            [10, 0, 12, 18, 22, 28],
            [20, 12, 0, 14, 16, 24],
            [15, 18, 14, 0, 10, 20],
            [30, 22, 16, 10, 0, 15],
            [25, 28, 24, 20, 15, 0]
        ]

    def test_sample_dataset_output_structure(self):
        """Kiem tra cau truc ket qua tra ve dung format ban giao cho TV 6."""
        cluster_A, cluster_B = divide_graph(
            self.n_sample, self.cost_matrix_sample, self.fame_sample, self.budget_sample
        )

        # Kiem tra moi cum gom dung 4 thanh phan: (nodes, cost_sub, fame_sub, budget_sub)
        self.assertEqual(len(cluster_A), 4)
        self.assertEqual(len(cluster_B), 4)

        nodes_A, cost_A, fame_A, budget_A = cluster_A
        nodes_B, cost_B, fame_B, budget_B = cluster_B

        # Kiem tra kieu du lieu
        self.assertIsInstance(nodes_A, list)
        self.assertIsInstance(cost_A, list)
        self.assertIsInstance(fame_A, list)
        self.assertIsInstance(budget_A, (int, float))

    def test_partition_independence_and_completeness(self):
        """Kiem tra 2 cum phan hoach doc lap, khong lap va khong chua diem 0."""
        for n, cost_mat, fame, budget in [
            (self.n_sample, self.cost_matrix_sample, self.fame_sample, self.budget_sample),
            (self.n_6, self.cost_matrix_6, self.fame_6, self.budget_6)
        ]:
            cluster_A, cluster_B = divide_graph(n, cost_mat, fame, budget)
            nodes_A, _, _, _ = cluster_A
            nodes_B, _, _, _ = cluster_B

            # Diem 0 khong duoc nam trong cum con (de danh cho buoc khoi dau va ket thuc)
            self.assertNotIn(0, nodes_A, "Diem 0 khong duoc co trong nodes_A")
            self.assertNotIn(0, nodes_B, "Diem 0 khong duoc co trong nodes_B")

            # 2 cum phai doc lap (khong giao nhau)
            set_A = set(nodes_A)
            set_B = set(nodes_B)
            self.assertTrue(set_A.isdisjoint(set_B), "nodes_A va nodes_B khong duoc chua diem trung nhau")

            # Hop 2 cum phai phu kin tap diem can tham quan
            all_expected_nodes = set(range(1, n))
            self.assertEqual(set_A.union(set_B), all_expected_nodes, "Hop 2 cum phai bang tap {1..n-1}")

    def test_submatrix_extraction_integrity(self):
        """Kiem tra ma tran con trich xuat chinh xac, dung kich thuoc va khong bi vuot qua gioi han chi so."""
        cluster_A, cluster_B = divide_graph(
            self.n_6, self.cost_matrix_6, self.fame_6, self.budget_6
        )

        for nodes_sub, cost_sub in [(cluster_A[0], cluster_A[1]), (cluster_B[0], cluster_B[1])]:
            sub_size = len(nodes_sub)
            # Kich thuoc ma tran con phai la sub_size x sub_size
            self.assertEqual(len(cost_sub), sub_size)
            for row in cost_sub:
                self.assertEqual(len(row), sub_size)

            # Gia tri trong ma tran con phai khop dung gia tri trong ma tran goc
            for i in range(sub_size):
                for j in range(sub_size):
                    orig_i = nodes_sub[i]
                    orig_j = nodes_sub[j]
                    self.assertEqual(
                        cost_sub[i][j],
                        self.cost_matrix_6[orig_i][orig_j],
                        f"cost_sub[{i}][{j}] phai bang cost_matrix_goc[{orig_i}][{orig_j}]"
                    )

            # Duong cheo bang 0
            for i in range(sub_size):
                self.assertEqual(cost_sub[i][i], 0.0)

    def test_subfame_extraction(self):
        """Kiem tra trich xuat mang fame con tuong ung chinh xac voi cac diem."""
        cluster_A, cluster_B = divide_graph(
            self.n_sample, self.cost_matrix_sample, self.fame_sample, self.budget_sample
        )
        nodes_A, _, fame_A, _ = cluster_A
        nodes_B, _, fame_B, _ = cluster_B

        # fame_A phai khop voi fame cac diem trong nodes_A
        expected_fame_A = [self.fame_sample[i] for i in nodes_A]
        expected_fame_B = [self.fame_sample[i] for i in nodes_B]

        self.assertEqual(fame_A, expected_fame_A)
        self.assertEqual(fame_B, expected_fame_B)

    def test_budget_allocation_and_reserve(self):
        """Kiem tra phan bo ngan sach va dam bao ngan sach du phong cho buoc combine."""
        budget = 1000000.0
        cluster_A, cluster_B = divide_graph(
            self.n_sample, self.cost_matrix_sample, self.fame_sample, budget
        )
        _, _, fame_A, budget_A = cluster_A
        _, _, fame_B, budget_B = cluster_B

        # Ngan sach du phong 20%
        reserve = budget * 0.2
        avail = budget - reserve

        # Tong ngan sach 2 cum phai bang available_budget
        self.assertAlmostEqual(budget_A + budget_B, avail, places=2)
        # Tong ngan sach 2 cum luon nho hon hoac bang budget goc
        self.assertLessEqual(budget_A + budget_B, budget)

        # Ti le ngan sach phai dung theo ti le tong fame
        sum_fame_A = sum(fame_A)
        sum_fame_B = sum(fame_B)
        total_fame = sum_fame_A + sum_fame_B
        expected_budget_A = (sum_fame_A / total_fame) * avail
        expected_budget_B = (sum_fame_B / total_fame) * avail

        self.assertAlmostEqual(budget_A, expected_budget_A, places=2)
        self.assertAlmostEqual(budget_B, expected_budget_B, places=2)

    def test_edge_case_zero_total_fame(self):
        """Kiem tra truong hop dac biet: Tat ca cac diem deu co fame = 0."""
        zero_fame = [0, 0, 0, 0]
        budget = 500000.0
        cluster_A, cluster_B = divide_graph(
            self.n_sample, self.cost_matrix_sample, zero_fame, budget
        )
        _, _, _, budget_A = cluster_A
        _, _, _, budget_B = cluster_B

        # Khi tong fame = 0, phan chia deu ngan sach kha dung
        avail = budget * 0.8
        self.assertAlmostEqual(budget_A, avail / 2.0, places=2)
        self.assertAlmostEqual(budget_B, avail / 2.0, places=2)

    def test_edge_case_zero_budget(self):
        """Kiem tra truong hop budget = 0."""
        cluster_A, cluster_B = divide_graph(
            self.n_sample, self.cost_matrix_sample, self.fame_sample, 0.0
        )
        _, _, _, budget_A = cluster_A
        _, _, _, budget_B = cluster_B

        self.assertEqual(budget_A, 0.0)
        self.assertEqual(budget_B, 0.0)

    def test_large_dataset_no_index_error(self):
        """Kiem tra tap du lieu lon (N=15) khong bi loi lech chi so."""
        n_large = 15
        cost_large = [[abs(i - j) * 100.0 for j in range(n_large)] for i in range(n_large)]
        fame_large = [0] + [i % 10 + 1 for i in range(1, n_large)]
        budget_large = 50000.0

        cluster_A, cluster_B = divide_graph(n_large, cost_large, fame_large, budget_large)
        nodes_A, cost_A, fame_A, budget_A = cluster_A
        nodes_B, cost_B, fame_B, budget_B = cluster_B

        self.assertEqual(len(nodes_A) + len(nodes_B), n_large - 1)
        self.assertEqual(len(cost_A), len(nodes_A))
        self.assertEqual(len(cost_B), len(nodes_B))
        self.assertEqual(len(fame_A), len(nodes_A))
        self.assertEqual(len(fame_B), len(nodes_B))
        self.assertLessEqual(budget_A + budget_B, budget_large)


if __name__ == '__main__':
    unittest.main()

