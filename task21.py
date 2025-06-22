def count_names(names: list[str]) -> dict[str, int] :
    """Ismlar sanash 
    
    ARGS:
        names (list[str]): Ismlar royhati
        
    Returns:
        dics[str , int]: natijasi
        
    """
    result = {}
    for name in names :
        result[name] = names.count(name)

    return result


name_list = ["Ali","Vali","Jon","Bob","Ali","Vali","Ali"]
result = count_names(name_list)
print(result)