import hashlib

def hash_gen(new_skill):
    """
    generates a hash value for the new skill using SHA256
    :input: skill
    :return:
        hash string for the input skill
    """
    skill_str = str(new_skill).strip().lower()
    skill_hash = hashlib.sha256(str.encode(skill_str)).hexdigest()
    return skill_hash

def df_to_dict(branchCol, leafCol):
    Dict = {}
    for abranch, aleaf in zip(branchCol, leafCol):
        if abranch not in Dict:
            Dict[abranch] = []
            Dict[abranch] += [aleaf]
        else:
            Dict[abranch] += [aleaf]
    return Dict