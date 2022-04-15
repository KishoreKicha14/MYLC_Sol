if not nums: return (-1, -1)
        
        # finding left most index (1st occurence) of target
        # when this function is called, r is already at the target (may not be the left most)
        # l is at the 1st index (0) and in this range all values are <= target
        def find_left(nums, l, r, target):
            while l < r:
                mid = l + (r - l) // 2
                if nums[mid] < target: l = mid + 1
                # As all values are <= target and previous if is is not entered,
                # That means nums[mid] == target now.
                # So, now if we find that nums[mid] is preceded by a smaller
                # Number, then that is the left most ocuurence of target
                elif nums[mid-1] < target: return mid
                # We are in the midst of target values
                # Reduce r to mid
                else: r = mid - 1
            return l
        
        # Finding right most index (last occurence) of target
        # When this function is called, l is already at the target (may not be the right most)
        # r is at the last index (len(nums)-1) and in this range all values are >= target
        def find_right(nums, l, r, target):
            while l < r:
                mid = l + (r - l) // 2
                if nums[mid] > target: r = mid - 1
                # As all values are >= target and previous if is is not entered,
                # That means nums[mid] == target now.
                # So, now if we find that nums[mid] is followe by a greater
                # number, then that is the right most ocuurence of target
                elif nums[mid+1] > target: return mid
                # We are in the midst of target values
                # Increase l to mid
                else: l = mid + 1
            return r
        
		# Binary search on whole array to find a random index of target
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] < target: l = mid + 1
            elif nums[mid] > target: r = mid - 1
            else: 
				# A random index of target is found
                return [find_left(nums, 0, mid, target), find_right(nums, mid, len(nums)-1, target)]
        return (-1, -1)
