// função e_int.js

var nums = [9, 1.1, 6, 2.0, 0, 0.3, 5, 3.1, 7.9, 9, 4];

for (var i = 0; i < nums.length; i++) {
    if (nums[i] % 1 !== 0) {
        print(nums[i], "não é inteiro");
    } else {
        print(nums[i], "é inteiro");
    }
}