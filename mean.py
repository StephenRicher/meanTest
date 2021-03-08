def mean(sample):
    """ Compute mean of list of numbers.
       
    Parameters
    ----------
    sample : List,
        List of numbers to compute mean
        
    Returns
    -------
    float
        Mean of sample.
    """
    assert len(sample) != 0, 'Unable to take the mean of an empty list.'
    for value in sample:
        if isinstance(value, complex):
            return NotImplemented
        assert isinstance(value, (int, float)), 'A value is not a number.'

    sample_mean = sum(sample) / len(sample)
    return sample_mean
    

def main():
    """
    Simple check of mean(num_list):
    calls mean on:
    numbers = [1, 2, 3, 4, 5],
    returning the mean, 3.0
    nonumbers = [], empty list
    which causes an assertion error
    word_and_numbers = [1, 2, 3, 4, "apple"], string in list
    which would raise assertion error is executed 
    """

    numbers = [1, 2, 3, 4, 5]
    print(mean(numbers))
    nonumbers = []
    print(mean(nonumbers))
    word_and_numbers = [1, 2, 3, 4, "apple"]
    print(mean(word_and_numbers))


if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
def mean_exc(num_list):
    if len(num_list) == 0 :
        raise Exception("The arithmetic mean of an empty list is undefined."
                         "Please provide a list of numbers")
    else :
        return sum(num_list) / len(num_list)
    

    
def mean_try_again(num_list):
    try:
        return sum(num_list) / len(num_list)
    except ZeroDivisionError:
        return 0
    except TypeError:
        print('The arithmetic mean of an non-numerical list is undefined. '
              'Please provide a list of numbers.')
        raise