n = len(nums)
从0 到n 一次产生长度为 0，1，2，。。。，n的子集，长度为0，1和n的可以直接获取，然后从 i in [2,n-1] 可以用 长度为i-1的子集在后面添加新的数字来得到长度为i的子集，整个过程中控制我们的数字是按大小排列，这样i-1的子集的最后一位是最大的数，只要添加比这个大的数字就不会出现重复