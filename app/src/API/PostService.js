import axios from 'axios'


const domain ='http://localhost:8000' 

const api = axios.create({baseURL: domain})

export default class PostService {    
    static async getUsersByGroupName(groupName, setUsers) {
        const response = await api.get(`/user/get_by_group/${groupName}/`)
        setUsers(response.data)
    }

    static async getWinnerFromUserList(userIdList, setWinner) {
        const response = await api.get(`/user/get_winner_from_user_list/`, {
            params: {
                user_id_list: userIdList
            }
        })
        setWinner(response.data)
    }
}