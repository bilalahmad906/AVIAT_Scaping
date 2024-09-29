import requests
from bs4 import BeautifulSoup


def get_direct_mount_links(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the 'Antennas' section
        antennas_section = soup.find('div', {'data-tab': 'menu-Antennas'})

        # Find the 'Direct Mount' section within 'Antennas'
        direct_mount_section = antennas_section.find('a', string='Direct Mount').find_parent('li')

        # Get all subclasses under 'Direct Mount'
        subclasses = [a.get_text() for a in direct_mount_section.find_all('a')[1:]]

        # Ask the user which subclass they are interested in
        print("Available subclasses under 'Direct Mount':")
        for i, subclass in enumerate(subclasses):
            print(f"{i + 1}. {subclass}")

        choice = int(input("Enter the number corresponding to your choice: ")) - 1
        selected_subclass = subclasses[choice]

        # Get all the links under the chosen subclass
        selected_subclass_section = direct_mount_section.find('a', string=selected_subclass).find_parent('li')
        selected_links = [a['href'] for a in selected_subclass_section.find_all('a')]

        return selected_links
    else:
        print(f"Failed to fetch the page. Status code: {response.status_code}")
        return None


if __name__ == "__main__":

    # Replace this URL with the actual URL of the page you want to scrape
    url = "https://aviat-store.aviatnetworks.com/"

    # Get the direct mount links
    links = get_direct_mount_links(url)
    if links:
        print("Links under the selected subclass:")
        for link in links:
            print(link)
