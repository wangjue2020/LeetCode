using DP, if current index i form a 个位数，then 只要不是0，就可以从i-1 导到 i， 如果form 一个两位数， then 只要i-1的位置上不是0且 i-1：i+1 组成的数字不超过26 就可以从i-2导到i， list l 记录到每一位的number of valid ways to decode， 每次按条件累加前一位和前两位，如果累加完依旧是0，说明无法decode