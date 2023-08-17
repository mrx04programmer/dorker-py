from googlesearch import search
class Dork:
    def search(query):
        results = []
        for j in search(query, num_results=20, proxy=None):
            results.append(j)
        return results

    def get_search_results_text(query):
        search_results = Dork.search(query)
        result_text = []
        for result in search_results:
            result_text.append(result)
        
        return result_text

    def main(query):
        results = Dork.get_search_results_text(query)
        for result in results:
            print(result)
            print("-"*len(result))
        