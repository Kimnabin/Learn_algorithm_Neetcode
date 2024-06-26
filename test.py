class Solution:
    def generateParentheses(self, n):
        result = []
        queue = [(0, 0, '')]  # Khởi tạo hàng đợi với số lượng dấu ngoặc trái, phải và chuỗi hiện tại
        
        while queue:
            left, right, s = queue.pop()
            
            # Nếu chuỗi đạt độ dài 2*n, thêm vào kết quả
            if len(s) == 2 * n:
                result.append(s)
                continue
            
            # Nếu số lượng dấu ngoặc trái hiện tại nhỏ hơn n, thêm dấu ngoặc trái mới
            if left < n:
                queue.append((left + 1, right, s + '('))
                
            # Nếu số lượng dấu ngoặc phải hiện tại nhỏ hơn số lượng dấu ngoặc trái, thêm dấu ngoặc phải mới
            if right < left:
                queue.append((left, right + 1, s + ')'))
        
        return result

# Test với n = 3
n = 3
print(Solution().generateParentheses(n))  

