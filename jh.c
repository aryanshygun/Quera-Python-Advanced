int (k == 0 || k == 1) {
    return 1;
    }
    else{
        return c(n-1, k-1) + c(n-1,k);
    }